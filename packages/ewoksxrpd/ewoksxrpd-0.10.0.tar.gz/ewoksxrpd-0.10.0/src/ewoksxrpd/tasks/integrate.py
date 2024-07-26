import os
import time
import logging
from numbers import Number
from contextlib import contextmanager, ExitStack
from typing import Sequence, Union, Tuple, List, Dict, Optional, Any

import numpy
import h5py
from ewoksdata.data.nexus import select_default_plot
from ewoksdata.data.hdf5.dataset_writer import DatasetWriter

from .worker import persistent_worker
from .worker import set_maximum_persistent_workers
from .log import zip_with_progress
from .utils import data_utils, xrpd_utils, pyfai_utils, integrate_utils
from .data_access import TaskWithDataAccess


__all__ = [
    "Integrate1D",
    "Integrate1DList",
    "IntegrateBlissScan",
    "IntegrateBlissScanWithoutSaving",
]


logger = logging.getLogger(__name__)


class _BaseIntegrate(
    TaskWithDataAccess,
    input_names=["detector", "geometry", "energy"],
    optional_input_names=[
        "detector_config",
        "mask",
        "flatfield",
        "darkcurrent",
        "integration_options",
        "fixed_integration_options",
        "maximum_persistent_workers",
        "references",
        "monitors",
        "demo",
    ],
    register=False,
):
    @contextmanager
    def _worker(self):
        nworkers = self.get_input_value("maximum_persistent_workers", None)
        if nworkers is not None:
            set_maximum_persistent_workers(nworkers)
        options = self._get_pyfai_options()
        with persistent_worker(options, self.get_input_value("demo", False)) as worker:
            yield worker, options

    def _get_pyfai_options(self) -> dict:
        geometry = data_utils.data_from_storage(self.inputs.geometry)
        xrpd_utils.validate_geometry(geometry)
        integration_options = data_utils.data_from_storage(
            self.inputs.integration_options, remove_numpy=True
        )
        fixed_integration_options = data_utils.data_from_storage(
            self.get_input_value("fixed_integration_options", None), remove_numpy=True
        )
        config = dict()
        if integration_options:
            config.update(integration_options)
        if fixed_integration_options:
            config.update(fixed_integration_options)
        if geometry:
            config.update(geometry)

        config.setdefault("unit", "2th_deg")
        config["detector"] = data_utils.data_from_storage(self.inputs.detector)
        config["detector_config"] = data_utils.data_from_storage(
            self.get_input_value("detector_config", None)
        )
        config["wavelength"] = xrpd_utils.energy_wavelength(self.inputs.energy)
        if not self.missing_inputs.mask and self.inputs.mask is not None:
            config["mask"] = self.get_image(
                data_utils.data_from_storage(self.inputs.mask)
            )
        if not self.missing_inputs.flatfield and self.inputs.flatfield is not None:
            config["flatfield"] = self.get_image(
                data_utils.data_from_storage(self.inputs.flatfield)
            )
        if not self.missing_inputs.darkcurrent and self.inputs.darkcurrent is not None:
            config["darkcurrent"] = self.get_image(
                data_utils.data_from_storage(self.inputs.darkcurrent)
            )
        return config

    def _pyfai_normalization_factor(
        self,
        monitors: List[Union[numpy.ndarray, Number, str, list, None]],
        references: List[Union[numpy.ndarray, Number, str, list, None]],
        ptdata: Optional[Dict[str, numpy.ndarray]] = None,
    ) -> Tuple[float, float]:
        r"""Returns the pyfai normalization factor based on a monitor and a references.

        The pyfai normalization factor is defined as

        .. code::

            Inorm = I / (normalization_factor1 * normalization_factor2 * ...)

        Monitor normalization is done like this

        .. code::

            Inorm = I * reference1 / monitor1 * reference2 / monitor2 * ...

        which means that the normalization factor is

        .. code::

            normalization_factor = monitor1 / reference1 * monitor2 / reference2 * ...

        Both monitors and references can be defined by:

         * scalar value
         * array or list of numbers
         * counter name
         * data URL
        """
        numerator = 1.0
        for value in monitors:
            if not data_utils.is_data(value):
                value = 1
            elif _is_counter_name(value):
                if ptdata is None:
                    raise ValueError("monitor value cannot be a counter name")
                value = ptdata[value]
            else:
                value = self.get_data(value)
            numerator *= value

        if not numpy.isscalar(numerator):
            raise ValueError("monitor values need to be scalars")

        denominator = 1.0
        for value in references:
            if not data_utils.is_data(value):
                value = 1
            elif _is_counter_name(value):
                if ptdata is None:
                    raise ValueError("reference value cannot be a counter name")
                value = ptdata[value]
            else:
                value = self.get_data(value)
            denominator *= value

        if not numpy.isscalar(denominator):
            raise ValueError("reference values need to be scalars")

        return numerator, denominator


class Integrate1D(
    _BaseIntegrate,
    input_names=["image"],
    optional_input_names=["monitor", "reference"],
    output_names=["x", "y", "yerror", "xunits", "info"],
):
    """1D integration of a single diffraction pattern."""

    def run(self):
        raw_data = self.get_image(self.inputs.image)

        monitors = self.get_input_value("monitors", list())
        references = self.get_input_value("references", list())
        if len(monitors) != len(references):
            raise ValueError(
                "length of normalization monitors and references is not the same"
            )
        if not self.missing_inputs.monitor or not self.missing_inputs.reference:
            monitors.append(self.get_input_value("monitor", None))
            references.append(self.get_input_value("reference", None))

        monitor_value, reference_value = self._pyfai_normalization_factor(
            monitors, references
        )
        normalization_factor = monitor_value / reference_value

        with self._worker() as (worker, config):
            result = worker.process(raw_data, normalization_factor=normalization_factor)

            self.outputs.x = result.radial
            self.outputs.y = result.intensity
            self.outputs.yerror = integrate_utils.get_yerror(result)
            self.outputs.xunits = result.unit.name

            info = pyfai_utils.compile_integration_info(
                config,
                monitor_value=monitor_value,
                reference_value=reference_value,
            )
            self.outputs.info = info


class Integrate1DList(
    _BaseIntegrate,
    input_names=["images", "output_file"],
    optional_input_names=["monitors", "references", "entry_name"],
    output_names=["output_uri"],
):
    """1D integration of a list of diffraction patterns."""

    def run(self):
        images: List[str] = self.inputs.images
        output_file: str = self.inputs.output_file
        monitors = self.get_input_value("monitors", [None] * len(images))
        references = self.get_input_value("references", [None] * len(images))
        entry_name = self.get_input_value("entry_name", "processing")

        with ExitStack() as stack:
            h5file = stack.enter_context(h5py.File(output_file, "a"))
            entry = h5file.require_group(entry_name)
            entry.attrs.setdefault("NX_class", "NXentry")
            process = entry.require_group("integrate")
            process.attrs["NX_class"] = "NXprocess"
            entry.attrs.setdefault("default", "integrate")

            worker, config = stack.enter_context(self._worker())

            info = pyfai_utils.compile_integration_info(
                config, monitors=monitors, references=references
            )
            nxtree_dict = pyfai_utils.integration_info_as_nxdict(info)
            pyfai_utils.dicttonx(
                nxtree_dict,
                output_file,
                h5path=process.name,
                update_mode="modify",
                mode="a",
            )

            intensity_writer = None
            error_writer = None

            for image, monitor, reference in zip_with_progress(
                images,
                monitors,
                references,
                message="Integrated %s images of %s",
                logger=logger,
            ):
                # Set mode to 'a' in case images are in `output_file`
                raw_data = self.get_image(image, mode="a")
                (monitor_value, reference_value) = self._pyfai_normalization_factor(
                    [monitor], [reference]
                )
                normalization_factor = monitor_value / reference_value

                result = worker.process(
                    raw_data, normalization_factor=normalization_factor
                )
                intensity_writer, error_writer, _ = integrate_utils.save_result(
                    result, intensity_writer, error_writer, process, stack
                )

            if intensity_writer is None:
                raise RuntimeError("No image data provided")
            intensity_writer.flush_buffer()
            if error_writer is not None:
                error_writer.flush_buffer()

            self.outputs.output_uri = f"{output_file}::{intensity_writer._parent.name}"


class IntegrateBlissScan(
    _BaseIntegrate,
    input_names=["filename", "scan", "detector_name", "output_filename"],
    optional_input_names=[
        "counter_names",
        "monitor_name",
        "reference",
        "subscan",
        "retry_timeout",
        "retry_period",
        "scan_memory_url",
        "external_output_filename",
        "nxprocess_name",
        "nxmeasurement_name",
        "nxprocess_as_default",
        "flush_period",
    ],
    output_names=["nxdata_url"],
):
    """1D or 2D integration of a single detector in a single Bliss scan with saving."""

    def run(self):
        if self.inputs.counter_names:
            counter_names = set(self.inputs.counter_names)
        else:
            counter_names = set()

        detector_name = self.inputs.detector_name

        monitors = self.get_input_value("monitors", list())
        references = self.get_input_value("references", list())
        if len(monitors) != len(references):
            raise ValueError(
                "length of normalization monitors and references is not the same"
            )
        if not self.missing_inputs.monitor_name or not self.missing_inputs.reference:
            monitors.append(self.get_input_value("monitor_name", None))
            references.append(self.get_input_value("reference", None))
        for name in references:
            if _is_counter_name(name):
                counter_names.add(name)
        for name in monitors:
            if _is_counter_name(name):
                counter_names.add(name)
        counter_names = list(counter_names)

        input_filename = os.path.abspath(self.inputs.filename)
        output_filename = os.path.abspath(self.inputs.output_filename)
        external_output_filename = os.path.abspath(
            self.get_input_value("external_output_filename", output_filename)
        )
        scan = self.inputs.scan
        subscan = self.get_input_value("subscan", 1)
        bliss_scan_url = data_utils.hdf5_url(input_filename, f"/{scan}.{subscan}")
        link_results_nxentry_url = data_utils.hdf5_url(
            output_filename, f"/{scan}.{subscan}"
        )
        results_nxentry_url = data_utils.hdf5_url(
            external_output_filename, f"/{scan}.{subscan}"
        )

        flush_period = self.get_input_value("flush_period", None)

        with ExitStack() as stack:
            worker = None
            results_nxentry = None
            link_results_nxentry = None
            results_nxprocess = None
            results_nxmeasurement = None

            intensity_writer = None
            error_writer = None
            ctr_writers = dict()

            if self.inputs.scan_memory_url:
                logger.info("PyFAI integrate data from %r", self.inputs.scan_memory_url)
                data_iterator = self.iter_bliss_data_from_memory(
                    self.inputs.scan_memory_url,
                    lima_names=[detector_name],
                    counter_names=counter_names,
                )
            else:
                logger.info(
                    "PyFAI integrate data from '%s::/%d.%d'",
                    self.inputs.filename,
                    self.inputs.scan,
                    subscan,
                )
                data_iterator = self.iter_bliss_data(
                    self.inputs.filename,
                    self.inputs.scan,
                    lima_names=[detector_name],
                    counter_names=counter_names,
                    subscan=subscan,
                )

            tstart = time.time()
            for (ptdata,) in zip_with_progress(
                data_iterator, message="Integrated %s images of %s", logger=logger
            ):
                if worker is None:
                    # Start the worker + open the output file only after
                    # the first image is read
                    worker, config = stack.enter_context(self._worker())
                    info = pyfai_utils.compile_integration_info(
                        config,
                        monitors=monitors,
                        references=references,
                    )
                    results_nxentry = stack.enter_context(
                        self.open_h5item(results_nxentry_url, mode="a", create=True)
                    )
                    assert isinstance(results_nxentry, h5py.Group)

                    with self.open_h5item(
                        link_results_nxentry_url, mode="a", create=True
                    ) as link_results_nxentry:
                        assert isinstance(link_results_nxentry, h5py.Group)
                        results_nxprocess = pyfai_utils.create_nxprocess(
                            results_nxentry,
                            link_results_nxentry,
                            self._nxprocess_name,
                            info,
                        )
                        results_nxmeasurement = results_nxentry.require_group(
                            "measurement"
                        )
                        results_nxmeasurement.attrs.setdefault(
                            "NX_class", "NXcollection"
                        )

                monitor_value, reference_value = self._pyfai_normalization_factor(
                    monitors, references, ptdata
                )
                normalization_factor = monitor_value / reference_value

                image = ptdata[detector_name]
                result = worker.process(
                    image, normalization_factor=normalization_factor
                )

                intensity_writer, error_writer, flush = integrate_utils.save_result(
                    result,
                    intensity_writer,
                    error_writer,
                    results_nxprocess,
                    stack,
                    flush_period,
                )
                for name in counter_names:
                    if name not in ctr_writers:
                        # This copies the raw counter names
                        ctr_writers[name] = stack.enter_context(
                            DatasetWriter(
                                results_nxmeasurement,
                                name,
                                flush_period=flush_period,
                            )
                        )
                    flush |= ctr_writers[name].add_point(ptdata[name])
                if flush:
                    results_nxentry.file.flush()

            if intensity_writer is None:
                tend = time.time()
                raise RuntimeError(
                    f"No scan data yielded within {tend-tstart:03f} from {bliss_scan_url}"
                )

            # Finalized writing
            intensity_writer.flush_buffer()
            if error_writer is not None:
                error_writer.flush_buffer()
            nxdata = intensity_writer._parent
            nxdata["points"] = numpy.arange(intensity_writer.dataset.shape[0])
            axes = nxdata.attrs["axes"]
            axes[0] = "points"
            nxdata.attrs["axes"] = axes

            # Create links
            with self.open_h5item(
                link_results_nxentry_url, mode="a", create=True
            ) as link_results_nxentry:
                data_utils.create_hdf5_link(
                    results_nxmeasurement,
                    self._nxmeasurement_name,
                    intensity_writer.dataset,
                )
                self.link_bliss_scan(link_results_nxentry, bliss_scan_url)
                if self.get_input_value("nxprocess_as_default", True):
                    select_default_plot(nxdata)
                link_nxmeasurement = link_results_nxentry.require_group("measurement")
                link_nxmeasurement.attrs.setdefault("NX_class", "NXcollection")
                data_utils.create_hdf5_link(
                    link_nxmeasurement,
                    self._nxmeasurement_name,
                    intensity_writer.dataset,
                )

            self.outputs.nxdata_url = f"{nxdata.file.filename}::{nxdata.name}"

    @property
    def _nxprocess_name(self) -> str:
        if self.inputs.nxprocess_name:
            return self.inputs.nxprocess_name
        group_name = "integrate"
        if self.inputs.detector_name:
            return f"{self.inputs.detector_name}_{group_name}"
        return group_name

    @property
    def _nxmeasurement_name(self) -> str:
        if self.inputs.nxmeasurement_name:
            return self.inputs.nxmeasurement_name
        link_name = "integrated"
        if self.inputs.detector_name:
            return f"{self.inputs.detector_name}_{link_name}"
        return link_name


class IntegrateBlissScanWithoutSaving(
    _BaseIntegrate,
    input_names=["filename", "scan", "detector_name"],
    optional_input_names=[
        "counter_names",
        "monitor_name",
        "reference",
        "subscan",
        "retry_timeout",
        "retry_period",
        "scan_memory_url",
    ],
    output_names=[
        "radial",
        "azimuthal",
        "intensity",
        "intensity_error",
        "radial_units",
        "azimuthal_units",
        "info",
    ],
):
    """1D or 2D integration of a single detector in a single Bliss scan without saving."""

    def run(self):
        with self._worker() as (worker, config):
            if self.inputs.counter_names:
                counter_names = set(self.inputs.counter_names)
            else:
                counter_names = set()
            detector_name = self.inputs.detector_name

            monitors = self.get_input_value("monitors", list())
            references = self.get_input_value("references", list())
            if len(monitors) != len(references):
                raise ValueError(
                    "length of normalization monitors and references is not the same"
                )
            if (
                not self.missing_inputs.monitor_name
                or not self.missing_inputs.reference
            ):
                monitors.append(self.get_input_value("monitor_name", None))
                references.append(self.get_input_value("reference", None))
            for name in references:
                if _is_counter_name(name):
                    counter_names.add(name)
            for name in monitors:
                if _is_counter_name(name):
                    counter_names.add(name)
            counter_names = list(counter_names)

            subscan = self.get_input_value("subscan", None)

            intensities = []
            sigmas = []
            radial = None
            radial_unit = None
            azimuthal = None
            azimuthal_unit = None

            if self.inputs.scan_memory_url:
                logger.info("PyFAI integrate data from %r", self.inputs.scan_memory_url)
                data_iterator = self.iter_bliss_data_from_memory(
                    self.inputs.scan_memory_url,
                    lima_names=[detector_name],
                    counter_names=counter_names,
                )
            else:
                logger.info(
                    "PyFAI integrate data from '%s::%d.%s'",
                    self.inputs.filename,
                    self.inputs.scan,
                    subscan,
                )
                data_iterator = self.iter_bliss_data(
                    self.inputs.filename,
                    self.inputs.scan,
                    lima_names=[detector_name],
                    counter_names=counter_names,
                    subscan=subscan,
                )

            normalization_factor = 0
            for (ptdata,) in zip_with_progress(
                data_iterator, message="Integrated %s images of %s", logger=logger
            ):
                monitor_value, reference_value = self._pyfai_normalization_factor(
                    monitors, references, ptdata
                )
                normalization_factor = monitor_value / reference_value
                image = ptdata[detector_name]
                result = worker.process(
                    image, normalization_factor=normalization_factor
                )

                intensities.append(result.intensity)
                sigmas.append(integrate_utils.get_yerror(result))
                if radial is None:
                    radial = result.radial
                if radial_unit is None:
                    radial_axis, azimuthal_axis = pyfai_utils.parse_pyfai_units(
                        result.unit
                    )
                    radial_unit = radial_axis.to_str()
                if worker.do_2D() and azimuthal is None:
                    azimuthal = result.azimuthal
                    azimuthal_unit = azimuthal_axis.to_str()

            info = pyfai_utils.compile_integration_info(
                config, monitors=monitors, references=references
            )

            self.outputs.radial = radial
            self.outputs.azimuthal = azimuthal
            self.outputs.intensity = numpy.array(intensities)
            self.outputs.intensity_error = numpy.array(sigmas)
            self.outputs.radial_units = radial_unit
            self.outputs.azimuthal_units = azimuthal_unit
            self.outputs.info = info


class MultiConfigIntegrate1D(
    _BaseIntegrate,
    input_names=["image", "configs"],
    optional_input_names=["monitor", "reference"],
    output_names=["x", "y", "yerror", "xunits", "info"],
):
    """1D integration of a single diffraction pattern."""

    def run(self):
        raw_data = self.get_image(self.inputs.image)
        configs: Sequence[dict] = self.inputs.configs

        monitors = self.get_input_value("monitors", list())
        references = self.get_input_value("references", list())
        if len(monitors) != len(references):
            raise ValueError(
                "length of normalization monitors and references is not the same"
            )
        if not self.missing_inputs.monitor or not self.missing_inputs.reference:
            monitors.append(self.get_input_value("monitor", None))
            references.append(self.get_input_value("reference", None))

        monitor_value, reference_value = self._pyfai_normalization_factor(
            monitors, references
        )
        normalization_factor = monitor_value / reference_value

        x = []
        y = []
        yerror = []
        infos = []
        units = []
        for config in configs:

            with self._worker() as (worker, initial_config):
                merged_config = {**initial_config, **config}
                worker.set_config(merged_config)
                result = worker.process(
                    raw_data, normalization_factor=normalization_factor
                )

                x.append(result.radial)
                y.append(result.intensity)
                yerror.append(integrate_utils.get_yerror(result))
                units.append(result.unit.name)

                infos.append(
                    pyfai_utils.compile_integration_info(
                        config,
                        monitor_value=monitor_value,
                        reference_value=reference_value,
                    )
                )

        self.outputs.x = x
        self.outputs.y = y
        self.outputs.yerror = yerror
        self.outputs.info = infos
        self.outputs.xunits = units


def _is_counter_name(value: Any) -> bool:
    return isinstance(value, str) and "://" not in value
