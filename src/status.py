from enum import Enum


class Status(Enum):
    INVALID = "invalid"
    VALID = "valid"
    GRANULARITY_STAGED = "granularity_staged"
    COVERAGE_STAGED = "coverage_staged"
