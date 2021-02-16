"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.
"""

from helpers import cd_to_datetime, datetime_to_str

__version__ = '2020.01.27.1101.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__info__ += '2nd submission, 1st did not pass pycodestyle 2.6.0'
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional),
    diameter in kilometers (optional - sometimes unknown), and whether it's
    marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the
         constructor.
        """
        self.designation = info.get('pdes', '')
        self.name = (lambda x: None if x == '' else x)(info.get('name'))
        self.diameter = (lambda x: float('nan') if x == ''
                         else float(x))(info.get('diameter', 0.0))
        self.hazardous = (lambda x: x == 'Y')(info.get('pha', 'N'))
        self.approaches = []

    def serialize(self):
        return {'designation': self.designation,
                'name': (lambda n: '' if n is None else n)(self.name),
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f"{self.designation} ({self.name})"

    def __str__(self):
        """Return `str(self)`."""
        hazardous = 'is' if self.hazardous else 'is not'
        diameter = self.diameter if self.diameter == self.diameter else 0.0
        return (f"NearEarthObject {self.fullname} has a diameter of "
                f"{diameter:.3f} km and {hazardous} potentially hazardous.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
        this object."""
        diameter = self.diameter if self.diameter == self.diameter else 0.0
        return (f"NearEarthObject(designation={self.designation!r}, "
                f"name={self.name!r}, diameter={diameter:.3f}, "
                f"hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to Earth, such as the date and time (in UTC) of closest approach, the
    nominal approach distance in astronomical units, and the relative approach
    velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the
        constructor.
        """
        self._designation = info.get('designation', '')
        self.time = cd_to_datetime(info.get('time'))
        self.distance = (lambda x: 0.0 if x == '' else
                         float(x))(info.get('distance', 0.0))
        self.velocity = (lambda x: 0.0 if x == '' else
                         float(x))(info.get('velocity', 0.0))
        self.neo = info.get('neo', None)

    def serialize(self):
        return {'datetime_utc': self.time_str,
                'distance_au': self.distance,
                'velocity_km_s': self.velocity}

    @property
    def designation(self):
        return self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach
        time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't exist
        in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return f"{datetime_to_str(self.time)}"

    def __str__(self):
        """Return `str(self)`."""
        return (f"A CloseApproach of {self._designation} at a distance of "
                f"{self.distance} au "
                f"and a velocity of {self.velocity} km/s on/at {self.time}")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
        this object."""
        return (f"CloseApproach(time={self.time_str!r}, "
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
