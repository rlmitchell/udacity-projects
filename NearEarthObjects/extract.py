"""Extract data on near-Earth objects and close approaches from CSV and
JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.
"""

import csv
import json
import sys
from models import NearEarthObject, CloseApproach

__version__ = '2020.01.27.1101.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__info__ += '2nd submission, 1st did not pass pycodestyle 2.6.0'
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about
    near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path) as csv_file:
        reader = csv.DictReader(csv_file)
        return tuple((NearEarthObject(pdes=row.get('pdes'),
                                      name=row.get('name'),
                                      diameter=row.get('diameter'),
                                      pha=row.get('pha')) for row in reader))


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as json_file:
        data = json.load(json_file)['data']
        return tuple((CloseApproach(designation=row[0],
                                    time=row[3],
                                    distance=row[4],
                                    velocity=row[7]) for row in data))
