# !usr/bin/python
# -*- coding: utf-8 -*-
import json

from enum import Enum


class Status(Enum):
    """
    Enum class with status for img extraction.
    """
    invalid = 1000
    coverage_staged = 100
    granularity_staged = 10
    valid = 1


def int_size(integer):
    return len("%i" % integer)


def read_json(json_filepath):
    with open(json_filepath) as json_file:
        data = json.load(json_file)
        return data
