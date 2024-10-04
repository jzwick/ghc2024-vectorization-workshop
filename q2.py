"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q2: Convert a dict to pd.DataFrame. Each key in the dict should become a column in the DataFrame.


def convert_dict_to_df(input_dict: dict):
    pass  # insert your code here


def make_test_dict(size: int = 100):
    return {
        chr(97 + i % 26) * (i // 26 + 1): np.random.rand(5) * 100 for i in range(size)
    }


def test_convert_dict(size: int = 1000):
    print("\n\nQ2: Running test_convert_dict...\n")
    input = make_test_dict(size)
    output = convert_dict_to_df(input)
    if output is not None:
        assert type(output) == pd.DataFrame and np.all(
            [key in output.columns for key in input.keys()]
        ), "Whoops! input and output do not match"
        print("  Success!")
    else:
        print("  convert_dict_to_df is not implemented")
