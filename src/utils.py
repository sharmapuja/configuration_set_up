#! /usr/bin/python3.8

""" Get Flattened Dictionary.

@file .py
@author Puja Sharma
@date 29th October 2021

About; -
--------
    This python module is responsible for generating flattened dictionary from python dictionary

Uses; -
-------

Reference; -
------------

"""
from collections.abc import MutableMapping


def flatten_dict(config_dict, parent_key='', sep='.'):
    """
    Generate flattened dictionary from nested dictionary

    :param sep:
    :param parent_key:
    :param config_dict: Nested Dictionary
    :type: Dict
    :return: Flattened Dictionary
    :rtype: Dict
    """
    items = []
    for k, v in config_dict.items():
        new_key = parent_key + sep + k if parent_key else k

        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)
