"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q6: Write a vectorized function, vec_pass_fail, which has the same arguments and returns as slow_pass_fail.
# (Hint: try using np.where and np.isin)


def slow_pass_fail(grades):
    pass_fail_grades = []
    for grade in grades:
        if grade == "A":
            pass_fail_grades.append("P")
        elif grade == "B":
            pass_fail_grades.append("P")
        elif grade == "C":
            pass_fail_grades.append("P")
        else:
            pass_fail_grades.append("F")

    return np.array(pass_fail_grades)


def vec_pass_fail(grades):
    pass  # insert your code here


def random_grades(num_grades: int):
    return np.random.randint(0, 100, size=num_grades)


def test_pass_fail(num_grades: int = 1000):
    print("\n\nQ6: Running test_pass_fail...\n")
    input = random_grades(num_grades)
    output_slow = pd.DataFrame(slow_pass_fail(input))
    output_vec = vec_pass_fail(input)
    if output_vec is not None:
        output_vec_df = pd.DataFrame(output_vec)
        pd.testing.assert_frame_equal(output_slow, output_vec_df, check_dtype=False)
        timings, _ = time_funcs(
            [slow_pass_fail, vec_pass_fail],
            [[input], [input]],
            ["slow_pass_fail", "vec_pass_fail"],
            reps=20,
        )
        print_time_results(timings, num_grades)
    else:
        print("  vec_pass_fail is not implemented")
