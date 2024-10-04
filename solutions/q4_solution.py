"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q4: Write a vectorized function, vec_addition, which adds two vectors of the same size


def slow_addition(arr1, arr2):
    assert len(arr1) == len(arr2)
    out = [a1 + a2 for a1, a2 in zip(arr1, arr2)]
    return np.array(out)


def vec_addition(arr1, arr2):
    return arr1 + arr2


def make_data1(size=1000):
    np.random.seed(4)
    array1 = np.random.rand(size, 1)  # np.array
    df1 = pd.DataFrame(array1)  # pd.DataFrame
    return df1


def test_addition(size=1000):
    print("\n\nQ4: Running test_addition...\n")
    input_1 = make_data1(size=size)
    input_2 = make_data1(size=size)
    output_slow = pd.DataFrame(slow_addition(input_1[0], input_2[0]))
    output_vec = vec_addition(input_1[0], input_2[0])
    if output_vec is not None:
        output_vec_df = pd.DataFrame(output_vec)
        pd.testing.assert_frame_equal(output_slow, output_vec_df, check_dtype=False)
        timings, _ = time_funcs(
            [slow_addition, vec_addition],
            [(input_1[0], input_2[0]), (input_1[0], input_2[0])],
            ["slow_addition", "vec_addition"],
            reps=20,
        )
        print_time_results(timings, size)
    else:
        print("  vec_addition is not implemented")
