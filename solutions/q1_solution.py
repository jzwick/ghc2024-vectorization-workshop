"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q1: Convert a list to np.array


def convert_list_to_array(input_list: list):
    return np.array(input_list)


def make_test_list(size: int = 100):
    return [i for i in range(size)]


def test_convert_list(size: int = 1000):
    print("\n\nQ1: Running test_convert_list...\n")
    input = make_test_list(size)
    output = convert_list_to_array(input)
    if output is not None:
        assert (
            type(output) == np.ndarray
            and len(input) == len(output)
            and np.all([input[i] == output[i] for i in range(len(input))])
        ), "Whoops! input and output do not match"
        print("  Success!")
    else:
        print("  convert_list_to_array is not implemented")
