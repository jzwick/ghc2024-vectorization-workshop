"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q3: Write a vectorized function vec_power which has the same arguments are returns as slow_power. Run the function on data1 and report your speedup on 20 reps


def slow_power(x, m=4):
    out = []
    for x_i in x:
        out.append(x_i**m)
    return np.array(out)


def vec_power(x, m=4):
    pass  # insert your new code here


def make_data1(size=1000):
    np.random.seed(4)
    array1 = np.random.rand(size, 1)  # np.array
    df1 = pd.DataFrame(array1)  # pd.DataFrame
    return df1


def test_power(size=1000):
    print("\n\nQ3: Running test_power...\n")
    input = make_data1(size=size)
    output_slow = pd.DataFrame(slow_power(input[0]))
    output_vec_raw = vec_power(input[0])
    if output_vec_raw is not None:
        output_vec = pd.DataFrame(output_vec_raw)
        pd.testing.assert_frame_equal(output_slow, output_vec, check_dtype=False)
        print("  Success!")
        timings, _ = time_funcs(
            [slow_power, vec_power],
            [[input[0]], [input[0]]],
            ["slow_power", "vec_power"],
            reps=20,
        )
        print_time_results(timings, size)
    else:
        print("  vec_power is not implemented")
