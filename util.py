### Utility helper functions for the vectorization workshop.###

import time

import numpy as np


def time_funcs(funcs, args, names, reps):
    """Returns dict of timing data for a list of functinos, arguments, and names.

    Args:
      funcs: list of functions to test
      args: list of arguments to the functions
      names: list of names of the functions. Will compare function with `slow` in the name vs those with `vec`
      reps: number of times to repeat the functions in computation of mean and std of timings

    Returns:
      timings: dict {name1:[time_elapsed, ...], name2:[time_elapsed, ...]..., }
      data
    """
    timings = {names[i]: [] for i in range(len(names))}
    data = {names[i]: None for i in range(len(names))}
    for j in range(reps):
        for i in range(len(funcs)):
            name = names[i]
            start = time.time()
            data[name] = funcs[i](*args[i])
            end = time.time()
            timings[name].append(end - start)
    timings["speedup"] = []
    for j in range(reps):
        slow_names = [name for name in names if "slow" in name]
        vec_names = [name for name in names if "vec" in name]
        timings["speedup"].append(
            max([timings[sn][j] for sn in slow_names])
            / min([timings[vn][j] for vn in vec_names])
        )
    return timings, data


def print_time_results(timings, data_size):
    """Given a timings object (output of time_funcs), print the results."""
    fstring = f'n_reps={len(timings["speedup"])}; data_size= {data_size} records\n'
    l = max([len(key) for key in timings.keys()])
    for key, value in timings.items():
        buff = l - len(key)
        if key == "speedup":
            fstring += f'{key}: {" "}{np.round(np.mean(value),1)}X  +/- {np.round(np.std(value),1)}X\n'
        else:
            fstring += f'{key}: {" "}{np.round(np.mean(value),4)}s +/- {np.round(np.std(value),4)}s\n'
    print(fstring)
