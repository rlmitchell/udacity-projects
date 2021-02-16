"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.
"""

import csv
import json

__version__ = '2020.01.27.1101.rlm'
__info__ = 'Adapted from/for Udemy\'s Python Nanodegree program. '
__info__ += '2nd submission, 1st did not pass pycodestyle 2.6.0'
__student__ = 'Rob Mitchell <rlmitchell@gmail.com>'


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output
    row corresponds to the information in a single close approach from the
    `results` stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s',
                  'designation', 'name', 'diameter_km',
                  'potentially_hazardous')
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for result in results:
            writer.writerow([result.time, result.distance, result.velocity,
                             result.designation, result.neo.name,
                             result.neo.diameter, result.neo.hazardous])


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output
    is a list containing dictionaries, each mapping `CloseApproach` attributes
    to their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be
    saved.
    """
    output = []
    for result in results:
        cainfo = result.serialize()
        cainfo.update({'neo': result.neo.serialize()})
        output.append(cainfo)

    with open(filename, 'w') as jsonfile:
        json.dump(output, jsonfile, indent=4)
