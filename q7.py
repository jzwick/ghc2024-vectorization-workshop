"""Unoptimized functions to be vectorized."""

import math
import time

import numpy as np
import pandas as pd

from util import print_time_results, time_funcs

# Q7: Write a vectorized function vec_insurance_factor which has the same arguments are returns as slow_insurance_factor_wrapper.


def slow_insurance_factor(car_df: pd.DataFrame):

    def slow_insurance_factor_row(year: int, color: str, model: str, mileage: float):
        """Return insurance factor based on car attributes."""
        factor = 1
        if year < 2000:
            factor *= 4
        elif year < 2015:
            factor *= 3
        elif year < 2020:
            factor *= 2
        if color in ["Red"]:
            factor *= 2
        if color == "Blue":
            factor *= 1.5
        factor += max((mileage - 100000) // 1000, 1)
        return factor

    return car_df.apply(
        lambda row: slow_insurance_factor_row(
            row["year"], row["color"], row["model"], row["mileage"]
        ),
        axis=1,
    )


def vec_insurance_factor(car_df: pd.DataFrame):
    pass  # insert your code here


class Car:
    def __init__(self, model: str, year: int, color: str, mileage: float):
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage


def make_car_list(n=1000):
    models = ["Sienna", "Corolla", "Forester", "Jetta", "Civic", "Escape", "Escalade"]
    colors = ["Black", "White", "Red", "Grey", "Blue"]
    years = range(1980, 2025)
    return [
        Car(
            model=np.random.choice(models),
            color=np.random.choice(colors),
            year=np.random.choice(years),
            mileage=np.random.random() * 200000,
        )
        for i in range(n)
    ]


def make_car_data(size: int = 1000):
    cars = make_car_list(n=size)
    df = pd.concat(
        [
            pd.DataFrame.from_dict(cars[i].__dict__, orient="index").transpose()
            for i in range(len(cars))
        ]
    )
    df.set_index(np.array(range(0,len(df))),inplace=True)
    return df


def test_insurance_factor(size: int = 1000):
    print("\n\nQ7: Running test_insurance_factor...\n")
    input = make_car_data(size)
    output_slow = pd.DataFrame(slow_insurance_factor(input))
    output_vec_raw = vec_insurance_factor(input)
    if output_vec_raw is not None:
        output_vec = pd.DataFrame(output_vec_raw)
        pd.testing.assert_frame_equal(output_slow, output_vec, check_dtype=False)
        timings, _ = time_funcs(
            [slow_insurance_factor, vec_insurance_factor],
            [[input], [input]],
            ["slow_insurance_factor", "vec_insurance_factor"],
            reps=20,
        )
        print_time_results(timings, size)
    else:
        print("  vec_insurance_factor is not implemented")
