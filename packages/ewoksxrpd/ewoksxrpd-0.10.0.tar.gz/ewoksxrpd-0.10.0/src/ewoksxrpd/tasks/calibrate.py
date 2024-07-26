from __future__ import annotations
import logging
import warnings
from numbers import Number
from typing import Dict, List, Optional, Set, Tuple, Sequence, Union, Generator

import pyFAI.detectors
import pyFAI.calibrant
import pyFAI.geometry
import pyFAI.goniometer
import pyFAI.geometryRefinement

from .utils import xrpd_utils
from .utils import data_utils
from .data_access import TaskWithDataAccess


__all__ = ["CalibrateSingle", "CalibrateMulti", "CalculateGeometry"]


logger = logging.getLogger(__name__)


def parse_fixed(
    fixed: Optional[List[str]], parametrization: Dict[str, List[str]]
) -> Set[str]:
    if not fixed:
        return set()
    allowed = {"dist", "poni1", "poni2", "rot1", "rot2", "rot3", "energy"}
    existing = set(fixed)
    unexpected = existing - allowed
    if unexpected:
        raise ValueError(f"'fixed' has unexpected parameters {sorted(unexpected)}")
    out = set()
    for param in fixed:
        out |= set(parametrization.get(param, {param}))
    return out


class CalibrateSingle(
    TaskWithDataAccess,
    input_names=["image", "detector", "calibrant", "geometry", "energy"],
    optional_input_names=[
        "detector_config",
        "fixed",
        "max_rings",
        "robust",
        "ring_detector",
    ],
    output_names=["geometry", "energy", "detector", "detector_config", "rings", "chi2"],
):
    """Single distance and energy calibration."""

    @property
    def _max_rings(self):
        max_rings = self.inputs.max_rings
        if not max_rings:
            return None
        if max_rings < 0:
            return None
        return max_rings

    def run(self):
        detector = data_utils.data_from_storage(self.inputs.detector)
        detector_config = data_utils.data_from_storage(
            self.get_input_value("detector_config", None)
        )
        detector_object = pyFAI.detectors.detector_factory(
            detector, config=detector_config
        )
        calibrant = data_utils.data_from_storage(self.inputs.calibrant)
        calibrant_object = pyFAI.calibrant.get_calibrant(calibrant)
        geometry0 = data_utils.data_from_storage(self.inputs.geometry)
        xrpd_utils.validate_geometry(geometry0)
        wavelength0 = xrpd_utils.energy_wavelength(self.inputs.energy)

        # Find diffraction rings and fit
        geometry_refinement = self._refine(
            dict(geometry0), wavelength0, calibrant_object, detector_object
        )

        # Parse results
        results = geometry_refinement.get_config()
        geometry = {
            k: v for k, v in results.items() if k in xrpd_utils.GEOMETRY_PARAMETERS
        }
        energy = xrpd_utils.energy_wavelength(results["wavelength"])
        rings = xrpd_utils.points_to_rings(geometry_refinement.data, calibrant_object)

        self.outputs.geometry = geometry
        self.outputs.energy = energy
        self.outputs.detector = detector
        self.outputs.detector_config = detector_config
        self.outputs.rings = rings
        if geometry_refinement.data.ndim != 2:
            self.outputs.chi2 = float("nan")
        else:
            self.outputs.chi2 = geometry_refinement.chi2()

    def _refine(
        self,
        geometry0: dict,
        wavelength0: float,
        calibrant: pyFAI.calibrant.Calibrant,
        detector: pyFAI.detectors.Detector,
    ) -> pyFAI.GeometryRefinement.GeometryRefinement:
        """Find diffraction rings and fit"""
        parametrization = {"energy": ["wavelength"]}
        force_fixed = parse_fixed(self.inputs.fixed, parametrization)
        all_parameters = xrpd_utils.GEOMETRY_PARAMETERS | {"wavelength"}

        if self.inputs.robust:
            parameter_release_groups = [
                {"dist"},
                {"poni1", "poni2"},
                {"rot1", "rot2", "rot3"},
                {"wavelength"},
            ]
        else:
            parameter_release_groups = [set(all_parameters)]

        # Initial fit parameters
        geometry = geometry0
        wavelength = wavelength0

        n = len(parameter_release_groups)
        it_fixed_parameters = _iter_fixed_parameters(
            all_parameters, force_fixed, parameter_release_groups
        )
        for i, fixed_parameters in enumerate(it_fixed_parameters, 1):
            # Detect experimental rings
            cps = self._extract_control_points(
                geometry, calibrant, wavelength, detector
            )

            # Fit parameters to detected rings
            setup = pyFAI.goniometer.SingleGeometry(
                "single_user_detector",
                detector=detector,
                geometry=geometry,
                calibrant=calibrant,
                control_points=cps,
            )
            setup.set_wavelength(wavelength)

            if cps is None:
                logger.warning("No rings detected for calibration")
                return setup.geometry_refinement

            _refine_geometry(
                setup.geometry_refinement, fixed_parameters=fixed_parameters
            )

            # Update parameters with fit result
            results = setup.geometry_refinement.get_config()
            geometry = {
                k: v for k, v in results.items() if k in xrpd_utils.GEOMETRY_PARAMETERS
            }
            wavelength = results["wavelength"]

            self.progress = i / n * 100

        return setup.geometry_refinement

    def _extract_control_points(
        self,
        geometry: dict,
        calibrant: pyFAI.calibrant.Calibrant,
        wavelength: float,
        detector: pyFAI.detectors.Detector,
    ) -> pyFAI.goniometer.ControlPoints | None:
        ring_detector_name = self.get_input_value("ring_detector", None)
        if ring_detector_name is None:
            ring_detector = detector
        else:
            ring_detector = pyFAI.detectors.detector_factory(ring_detector_name)

        setup = pyFAI.goniometer.SingleGeometry(
            "single_ring_detector",
            image=self.get_image(self.inputs.image),
            detector=ring_detector,
            geometry=geometry,
            calibrant=calibrant,
        )
        setup.set_wavelength(wavelength)

        setup.extract_cp(max_rings=self._max_rings)
        if setup.geometry_refinement.data.ndim != 2:
            logger.warning("No rings detected for calibration")
            return

        return setup.control_points


class CalibrateMulti(
    TaskWithDataAccess,
    input_names=[
        "images",
        "positions",
        "detector",
        "calibrant",
        "geometry",
        "energy",
    ],
    optional_input_names=[
        "reference_position",
        "sample_position",
        "positionunits_in_meter",
        "detector_config",
        "fixed",
        "max_rings",
        "robust",
    ],
    output_names=[
        "geometry",
        "energy",
        "detector",
        "detector_config",
        "rings",
        "chi2",
        "parametrization",
        "parameters",
    ],
):
    """Single energy, multi distance calibration with 1 distance motor.

    The `images` and `positions` are the diffraction patterns and the motor positions at which those were measured.

    The `reference_position` is the detector position that corresponds to `geometry` (`positions[0]` by default).

    The `sample_position` is the position where sample and detector would theoretically coincide (0 by default).

    The output `energy` and `geometry` correspond to `sample_position`.

    The units of `positions`, `sample_position` and `reference_position` are defined by `positionunits_in_meter`
    (1e-3 by default which means the unit is in millimeter).

    The parametrization allow deriving energy+geometry from the detector position.

    .. code-block:: python

        energy, geometry = parametrization(parameters, position)
    """

    def run(self):
        if len(self.inputs.images) != len(self.inputs.positions):
            raise ValueError("number of 'images' and 'positions' must be the same")
        detector = data_utils.data_from_storage(self.inputs.detector)
        detector_config = data_utils.data_from_storage(
            self.get_input_value("detector_config", None)
        )
        detector_object = pyFAI.detectors.detector_factory(
            detector, config=detector_config
        )
        calibrant = data_utils.data_from_storage(self.inputs.calibrant)
        calibrant_object = pyFAI.calibrant.get_calibrant(calibrant)
        energy0 = self.inputs.energy
        wavelength0 = xrpd_utils.energy_wavelength(energy0)
        geometry0 = data_utils.data_from_storage(self.inputs.geometry)
        xrpd_utils.validate_geometry(geometry0)

        # Parameterize the detector geometry
        trans_function, initial_guess = self._reparametrization(geometry0, energy0)

        # Define setup
        setup = pyFAI.goniometer.GoniometerRefinement(
            initial_guess,
            pos_function=lambda x: x,
            trans_function=trans_function,
            detector=detector_object,
            wavelength=wavelength0,
        )
        for i, (image, xi) in enumerate(zip(self.inputs.images, self.inputs.positions)):
            label = f"position{i}"
            image = self.get_image(image)
            xi = self.get_data(xi)
            setup.new_geometry(
                label, image=image, metadata=xi, calibrant=calibrant_object
            )

        # Find diffraction rings and fit
        self._refine(setup)

        # Parse results
        geometry, energy = self._get_fit_results(setup)
        paramerization = self._get_parameterization(setup)
        parameters = self._get_parameters(setup)
        rings = self._get_rings(setup, calibrant_object)
        chi2 = setup.chi2()

        self.outputs.geometry = geometry
        self.outputs.energy = energy
        self.outputs.detector = detector
        self.outputs.detector_config = detector_config
        self.outputs.rings = rings
        self.outputs.chi2 = chi2
        self.outputs.parametrization = paramerization
        self.outputs.parameters = parameters

    def _reparametrization(
        self, geometry0: Dict, energy0: float
    ) -> Tuple[pyFAI.goniometer.ExtendedTransformation, List[Number]]:
        # xunits are the position units
        # dunits are the distance units of the fit parameters
        # aunits are the angular units of the fit parameters
        dunits_per_m = 100  # dunits/m
        aunits_per_rad = 10  # aunits/rad
        m_per_xunits = self._get_position_units()  # m/xunits

        trans_function = pyFAI.goniometer.ExtendedTransformation(
            param_names=[
                "dist_offset",  # dunits
                "dist_scale",  # dunits/xunits
                "poni1_offset",  # dunits
                "poni1_scale",  # dunits/xunits
                "poni2_offset",  # dunits
                "poni2_scale",  # dunits/xunits
                "arot1",  # aunits
                "arot2",  # aunits
                "arot3",  # aunits
                "energy",  # keV
            ],
            pos_names=["x"],  # xunits
            dist_expr=f"dist_scale / {dunits_per_m} * x + dist_offset / {dunits_per_m}",
            poni1_expr=f"poni1_scale / {dunits_per_m} * x + poni1_offset / {dunits_per_m}",
            poni2_expr=f"poni2_scale / {dunits_per_m} * x + poni2_offset / {dunits_per_m}",
            rot1_expr=f"arot1 / {aunits_per_rad}",
            rot2_expr=f"arot2 / {aunits_per_rad}",
            rot3_expr=f"arot3 / {aunits_per_rad}",
            wavelength_expr="hc*1e-10/energy",
        )

        xref = self._get_reference_position()  # xunits
        dist_offset = self._get_sample_position() * m_per_xunits  # m
        dist_scale = (geometry0["dist"] - dist_offset) / xref  # m/xunits

        poni1_scale = 0.0  # m/xunits
        poni1_offset = geometry0["poni1"]  # m
        poni2_scale = 0.0  # m/xunits
        poni2_offset = geometry0["poni2"]  # m

        initial_guess = [
            dist_offset * dunits_per_m,
            dist_scale * dunits_per_m,
            poni1_offset * dunits_per_m,
            poni1_scale * dunits_per_m,
            poni2_offset * dunits_per_m,
            poni2_scale * dunits_per_m,
            geometry0["rot1"] * aunits_per_rad,
            geometry0["rot2"] * aunits_per_rad,
            geometry0["rot3"] * aunits_per_rad,
            energy0,
        ]
        return trans_function, initial_guess

    @property
    def _max_rings(self):
        max_rings = self.inputs.max_rings
        if not max_rings:
            return None
        if max_rings < 0:
            return None
        return max_rings

    def _refine(self, setup: pyFAI.goniometer.GoniometerRefinement) -> None:
        """Find diffraction rings and fit"""
        parametrization = {
            "dist": ["dist_offset", "dist_scale"],
            "poni1": ["poni1_offset", "poni1_scale"],
            "poni2": ["poni2_offset", "poni2_scale"],
            "rot1": ["arot1"],
            "rot2": ["arot2"],
            "rot3": ["arot3"],
        }
        force_fixed = parse_fixed(self.inputs.fixed, parametrization)
        all_parameters = set(setup.trans_function.param_names)

        if self.inputs.robust:
            parameter_release_groups = [
                {"dist_offset", "dist_scale"},
                {"poni1_offset", "poni2_offset"},
                {"arot1", "arot2", "arot3"},
                {"poni1_scale", "poni2_scale"},
                {"energy"},
            ]
        else:
            parameter_release_groups = [set(all_parameters)]

        n = len(parameter_release_groups)
        it_fixed_parameters = _iter_fixed_parameters(
            all_parameters, force_fixed, parameter_release_groups
        )
        for i, fixed_parameters in enumerate(it_fixed_parameters, 1):
            # Detect experimental rings
            for setup_single_dist in setup.single_geometries.values():
                setup_single_dist.extract_cp(max_rings=self._max_rings)
                if setup_single_dist.geometry_refinement.data.ndim != 2:
                    logger.warning("No rings detected for calibration")
                    return

            # Fit parameters to detected rings
            _refine_geometry(setup, fixed_parameters=fixed_parameters)

            self.progress = i / n * 100

    def _get_rings(
        self,
        setup: pyFAI.goniometer.GoniometerRefinement,
        calibrant: pyFAI.calibrant.Calibrant,
    ) -> Dict[str, dict]:
        rings = dict()
        for i, setup_single_dist in enumerate(setup.single_geometries.values()):
            points = setup_single_dist.geometry_refinement.data
            rings[str(i)] = xrpd_utils.points_to_rings(points, calibrant)
        return rings

    def _get_fit_results(
        self, setup: pyFAI.goniometer.GoniometerRefinement
    ) -> Tuple[dict, Number]:
        parameters = setup.param
        xref = self._get_reference_position()
        results = setup.trans_function(parameters, xref)
        geometry = {k: getattr(results, k) for k in xrpd_utils.GEOMETRY_PARAMETERS}
        energy = xrpd_utils.energy_wavelength(results.wavelength)
        return geometry, energy

    def _get_parameterization(
        self, setup: pyFAI.goniometer.GoniometerRefinement
    ) -> dict:
        parametrization = dict(setup.trans_function.to_dict())
        parametrization.pop("constants")
        parametrization.pop("content")
        return parametrization

    def _get_parameters(self, setup: pyFAI.goniometer.GoniometerRefinement) -> dict:
        parameters = setup.param
        names = setup.trans_function.param_names
        return dict(zip(names, parameters))

    def _get_reference_position(self):
        """first image position by default (xunits)"""
        if self.missing_inputs.reference_position:
            return self.get_data(self.inputs.positions[0])
        else:
            return self.get_data(self.inputs.reference_position)

    def _get_sample_position(self):
        """0 by default (xunits)"""
        if self.missing_inputs.sample_position:
            return 0
        else:
            return self.get_data(self.inputs.sample_position)

    def _get_position_units(self):
        """millimeter by default"""
        if self.inputs.positionunits_in_meter:
            return self.inputs.positionunits_in_meter  # m/xunits
        else:
            return 1e-3  # m/xunits


def calculate_geometry(
    parametrization: dict, parameters: dict, position: Number
) -> Tuple[dict, Number]:
    trans_function = pyFAI.goniometer.ExtendedTransformation(**parametrization)
    parameters = [parameters[name] for name in trans_function.param_names]
    trans_function(parameters, position)
    results = trans_function(parameters, position)
    geometry = {k: getattr(results, k) for k in xrpd_utils.GEOMETRY_PARAMETERS}
    energy = xrpd_utils.energy_wavelength(results.wavelength)
    return geometry, energy


class CalculateGeometry(
    TaskWithDataAccess,
    input_names=["parametrization", "parameters", "position"],
    output_names=["geometry", "energy"],
):
    """Calculate energy and geometry from pyFAI parametrization"""

    def run(self):
        parametrization = data_utils.data_from_storage(self.inputs.parametrization)
        geometry, energy = calculate_geometry(
            parametrization,
            self.inputs.parameters,
            self.get_data(self.inputs.position),
        )
        self.outputs.geometry = geometry
        self.outputs.energy = energy


def _iter_fixed_parameters(
    all_parameters: Set[str],
    force_fixed: Set[str],
    parameter_release_groups: Sequence[Set[str]],
) -> Generator[Optional[Set[str]], None, None]:
    """Start with all parameters fixed. Release parameters in groups and yield the fixed parameters after each iteration.

    :param all_parameters: all parameters
    :param force_fixed: parameters that are always fixed
    :param parameter_release_groups: groups of parameters to release in each iteration
    :yield: fixed parameters for each iteration
    """
    fixed_parameters = all_parameters
    for release_group in parameter_release_groups:
        release = release_group - force_fixed
        if release:
            fixed_parameters -= release
            yield fixed_parameters
        else:
            yield None


def _refine_geometry(
    geometry_refinement: Union[
        pyFAI.goniometer.GoniometerRefinement,
        pyFAI.geometryRefinement.GeometryRefinement,
    ],
    fixed_parameters: Optional[Sequence] = None,
) -> bool:
    """
    Refines the given geometry within the default parameter bounds.

    :param geometry_refinement: A pyFAI object that parameterizes a single or multi-distances geometry.
    :param fixed_parameters: Parameters that are not allowed to change during refinement.
    :return: True if refinement is successful within the default parameter bounds, False otherwise.
    """
    with warnings.catch_warnings(record=True) as caught_warnings:
        warnings.filterwarnings(
            "always",
            message="Values in x were outside bounds during a minimize step, clipping to bounds",
            category=RuntimeWarning,
        )
        geometry_refinement.refine3(fix=fixed_parameters)  # method="slsqp"
        if not caught_warnings:
            return True

    return False
