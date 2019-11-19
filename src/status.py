from enum import Enum


class Status(Enum):
    invalid = 1000
    coverage_staged = 100
    granularity_staged = 10
    valid = 1
