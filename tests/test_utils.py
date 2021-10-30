"""Unit test for test_utils.py module.

@file test_utils.py
@author Puja Sharma
@date 30th October 2021

About; -
--------
    This python module is responsible for testing the utils.py
    Test flattened dict is generated from nested dict.

Uses; -
-------

Reference; -
------------

"""

from src.utils import flatten_dict
from tests.config.sample_dictionary import test_config_dict, flattened_dict


def test_flattened_dict():
    """ Test flattened dictionary is generated from nested dictionary"""

    response = flatten_dict(test_config_dict)
    assert response == flattened_dict
