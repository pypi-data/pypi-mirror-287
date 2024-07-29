import pytest
import regex_sampler


def test_sum_as_string():
    assert regex_sampler.sum_as_string(1, 1) == "2"
