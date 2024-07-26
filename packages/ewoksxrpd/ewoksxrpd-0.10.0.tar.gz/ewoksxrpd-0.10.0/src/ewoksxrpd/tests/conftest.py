import os
import h5py
import pytest
import numpy

import pyFAI.azimuthalIntegrator
import pyFAI.detectors
from ewoksorange.canvas.handler import OrangeCanvasHandler
from ewoksorange.tests.conftest import qtapp  # noqa F401
from ewoksdata.tests.data import save_bliss_scan

from . import xrpd_theory


@pytest.fixture(scope="session")
def setup1() -> xrpd_theory.Setup:
    # Detector size is approx. 0.18 x 0.18 m
    geometry = {
        "dist": 10e-2,  # 10 cm
        "poni1": 10e-2,  # 10 cm
        "poni2": 10e-2,  # 10 cm
        "rot1": numpy.radians(10),  # 10 deg
        "rot2": 0,  # 0 deg
        "rot3": 0,  # 0 deg
    }
    return xrpd_theory.Setup(detector="Pilatus1M", energy=12, geometry=geometry)


@pytest.fixture(scope="session")
def setup2(setup1) -> xrpd_theory.Setup:
    # setup1 with detector shifted 5 cm backwards
    geometry = dict(setup1.geometry)
    geometry["dist"] += 5e-2
    assert geometry["dist"] > 0
    return xrpd_theory.Setup(
        detector=setup1.detector, energy=setup1.energy, geometry=geometry
    )


@pytest.fixture(scope="session")
def aiSetup1(
    setup1: xrpd_theory.Setup,
) -> pyFAI.azimuthalIntegrator.AzimuthalIntegrator:
    detector = pyFAI.detectors.detector_factory(setup1.detector)
    return pyFAI.azimuthalIntegrator.AzimuthalIntegrator(
        detector=detector, **setup1.geometry
    )


@pytest.fixture(scope="session")
def aiSetup2(
    setup2: xrpd_theory.Setup,
) -> pyFAI.azimuthalIntegrator.AzimuthalIntegrator:
    detector = pyFAI.detectors.detector_factory(setup2.detector)
    return pyFAI.azimuthalIntegrator.AzimuthalIntegrator(
        detector=detector, **setup2.geometry
    )


def linspace(low_limit, high_limit, n):
    half_bin = (high_limit - low_limit) / (2 * n)
    return numpy.linspace(low_limit + half_bin, high_limit - half_bin, n)


@pytest.fixture(scope="session")
def xSampleA() -> xrpd_theory.xPattern:
    x = linspace(0, 30, 1024)
    return xrpd_theory.xPattern(x=x, low_limit=0, high_limit=30, units="2th_deg")


@pytest.fixture(scope="session")
def ySampleA(xSampleA: xrpd_theory.xPattern) -> xrpd_theory.yPattern:
    x = xSampleA.x
    y = numpy.zeros(x.size)
    peaks = list()
    s = 0.5
    for ufrac in [0.1, 0.4, 0.7]:
        A = 100
        u = x[0] + ufrac * (x[-1] - x[0])
        y += (
            A * numpy.exp(-((x - u) ** 2) / (2 * s**2)) / (s * numpy.sqrt(2 * numpy.pi))
        )
        peaks.append((A, u, s))
    return xrpd_theory.yPattern(y=y, monitor=1000, theory=peaks)


@pytest.fixture(scope="session")
def xSampleB() -> xrpd_theory.xPattern:
    x = linspace(0, 180, 1024)
    return xrpd_theory.xPattern(x=x, low_limit=0, high_limit=180, units="2th_deg")


@pytest.fixture(scope="session")
def ySampleB(xSampleB: xrpd_theory.xPattern) -> xrpd_theory.yPattern:
    y = numpy.full(xSampleB.x.size, 10)
    return xrpd_theory.yPattern(y=y, monitor=1000, theory=10)


@pytest.fixture(scope="session")
def imageSetup1SampleA(
    aiSetup1: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    xSampleA: xrpd_theory.xPattern,
    ySampleA: xrpd_theory.yPattern,
) -> xrpd_theory.Measurement:
    return xrpd_theory.measurement(aiSetup1, xSampleA, ySampleA, mult=2)


@pytest.fixture(scope="session")
def imageSetup2SampleA(
    aiSetup2: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    xSampleA: xrpd_theory.xPattern,
    ySampleA: xrpd_theory.yPattern,
) -> xrpd_theory.Measurement:
    return xrpd_theory.measurement(aiSetup2, xSampleA, ySampleA, mult=2)


@pytest.fixture(scope="session")
def image1Setup1SampleB(
    aiSetup1: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    xSampleB: xrpd_theory.xPattern,
    ySampleB: xrpd_theory.yPattern,
) -> xrpd_theory.Measurement:
    return xrpd_theory.measurement(aiSetup1, xSampleB, ySampleB, mult=2)


@pytest.fixture(scope="session")
def image2Setup1SampleB(
    aiSetup1: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    xSampleB: xrpd_theory.xPattern,
    ySampleB: xrpd_theory.yPattern,
) -> xrpd_theory.Measurement:
    return xrpd_theory.measurement(aiSetup1, xSampleB, ySampleB, mult=3)


@pytest.fixture(scope="session")
def imageSetup1Calibrant1(
    aiSetup1: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    setup1: xrpd_theory.Setup,
) -> xrpd_theory.Calibration:
    return xrpd_theory.calibration("LaB6", aiSetup1, setup1)


@pytest.fixture(scope="session")
def imageSetup2Calibrant1(
    aiSetup2: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    setup2: xrpd_theory.Setup,
) -> xrpd_theory.Calibration:
    return xrpd_theory.calibration("LaB6", aiSetup2, setup2)


def next_scan_number(filename) -> int:
    if not os.path.exists(filename):
        return 1
    with h5py.File(filename, "r") as h5file:
        return int(max(map(float, h5file.keys()))) + 1


@pytest.fixture(scope="session")
def ewoks_orange_canvas(qtapp):  # noqa F811
    with OrangeCanvasHandler() as handler:
        yield handler


@pytest.fixture(scope="session")
def bliss_lab6_scan(tmpdir_factory, imageSetup1Calibrant1):
    tmpdir = tmpdir_factory.mktemp("sample_dataset")
    npoints_per_file = 3
    npoints = 31
    scannr = 2
    image = imageSetup1Calibrant1.image
    return save_bliss_scan(
        tmpdir,
        image,
        npoints_per_file,
        npoints,
        scannr,
        subscannr=1,
        lima_names=("p3",),
        counter_names=("diode1", "diode2"),
        sequence="multiply",
    )


@pytest.fixture(scope="session")
def bliss_perkinelmer_scan(tmpdir_factory, imageSetup1Calibrant1):
    tmpdir = tmpdir_factory.mktemp("sample_dataset")
    npoints_per_file = 3
    npoints = 31
    scannr = 2
    image = imageSetup1Calibrant1.image
    return save_bliss_scan(
        tmpdir,
        image,
        npoints_per_file,
        npoints,
        scannr,
        subscannr=1,
        lima_names=("perkinelmer",),
        counter_names=("mon",),
        sequence="multiply",
    )


@pytest.fixture(scope="session")
def bliss_task_inputs(bliss_lab6_scan, setup1) -> dict:
    return {
        "filename": str(bliss_lab6_scan),
        "scan": 2,
        "detector": setup1.detector,
        "energy": setup1.energy,
        "geometry": setup1.geometry,
        "detector_name": "p3",
        "monitor_name": "monitor",
        "reference": 1.0,
        "retry_timeout": 2,
    }


@pytest.fixture(autouse=True)
def matplotlib_cleanup():
    """Use this in tests that use matplotlib without ewoksorange.tests.conftest.qtapp"""
    yield
    try:
        from matplotlib.backends import backend_qt

        backend_qt.qApp = None
        backend_qt._create_qApp.cache_clear()
    except (ImportError, AttributeError):
        pass
