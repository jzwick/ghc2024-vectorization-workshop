"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q5: Write a vectorized function, vec_grade, which has the same arguments and return as slow_grade.
# Note that when evaluating multiple boolean conditions over a vector, bitwise operators must be used
# Example: indices_of_nums_bt_1_and_5 = (some_other_vector > 1) & (some_other_vector < 5)


def slow_grade(grades):
    letter_grades = []
    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif 80 <= grade <= 90:
            letter_grades.append("B")
        elif 70 <= grade <= 80:
            letter_grades.append("C")
        elif grade < 70:
            letter_grades.append("F")

    return np.array(letter_grades)


def vec_grade(grades):
    pass  # insert your code here


def random_grades(num_grades: int):
    return np.random.randint(0, 100, size=num_grades)


def test_grades(num_grades: int = 1000):
    print("\n\nQ5: Running test_grades...\n")
    input = random_grades(num_grades)
    output_slow = pd.DataFrame(slow_grade(input))
    output_vec = vec_grade(input)
    if output_vec is not None:
        output_vec_df = pd.DataFrame(output_vec)
        pd.testing.assert_frame_equal(output_slow, output_vec_df, check_dtype=False)
        timings, _ = time_funcs(
            [slow_grade, vec_grade],
            [[input], [input]],
            ["slow_grade", "vec_grade"],
            reps=20,
        )
        print_time_results(timings, num_grades)
    else:
        print("  vec_grade is not implemented")
