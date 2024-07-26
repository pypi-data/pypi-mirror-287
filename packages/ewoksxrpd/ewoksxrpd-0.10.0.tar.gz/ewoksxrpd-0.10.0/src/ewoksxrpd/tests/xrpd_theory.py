from dataclasses import dataclass, field
from typing import Any
from numpy.typing import ArrayLike
import numpy
import pyFAI.units
import pyFAI.azimuthalIntegrator
import pyFAI.calibrant


@dataclass(frozen=True)
class xPattern:
    x: ArrayLike = field(repr=False)
    low_limit: float
    high_limit: float
    units: str

    @property
    def integration_options(self) -> dict:
        return {
            "radial_range_min": self.low_limit,
            "radial_range_max": self.high_limit,
            "nbpt_rad": self.x.size,
            "unit": self.units,
        }


@dataclass(frozen=True)
class yPattern:
    y: ArrayLike = field(repr=False)
    monitor: float
    theory: Any


@dataclass(frozen=True)
class Measurement:
    image: ArrayLike = field(repr=False)
    monitor: float


@dataclass(frozen=True)
class Calibration:
    image: ArrayLike = field(repr=False)
    calibrant: str


@dataclass(frozen=True)
class Setup:
    detector: str
    energy: float  # keV
    geometry: dict

    @property
    def wavelength(self) -> float:  # Angstrom
        return pyFAI.units.hc / (self.energy * 1e10)


def calibration(
    name: str, ai: pyFAI.azimuthalIntegrator.AzimuthalIntegrator, setup: Setup
) -> Calibration:
    calibrant = pyFAI.calibrant.get_calibrant(name)
    calibrant.set_wavelength(setup.wavelength)
    # W = FWHM^2 in rad
    FWHM = 0.2  # deg
    W = numpy.radians(FWHM) ** 2
    image = calibrant.fake_calibration_image(ai, Imax=100, W=W)
    return Calibration(image=image, calibrant=name)


def measurement(
    ai: pyFAI.azimuthalIntegrator.AzimuthalIntegrator,
    xpattern,
    ypattern,
    mult=2,
):
    x = xpattern.x
    y = mult * ypattern.y
    monitor = mult * ypattern.monitor
    image = ai.calcfrom1d(x, y, dim1_unit=xpattern.units, mask=ai.mask)
    return Measurement(image=image, monitor=monitor)
