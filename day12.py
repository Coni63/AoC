"""
PART I: Ok but too slow for part 2
"""

from itertools import combinations, groupby
from functools import lru_cache
import time


with open('input12.txt') as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

ans = 0

for line in lines:
    row, vals = line.split()
    vals = [int(x) for x in vals.split(",")]
    row = list(row)

    position_used = [i for i, x in enumerate(row) if x == "#"]
    missing = sum(vals) - len(position_used)  # number of missing #

    position_to_tests = [i for i, x in enumerate(row) if x == "?"]
    for rep in combinations(position_to_tests, missing):
        for i in position_to_tests:
            row[i] = "." if i not in rep else "#"

        seq = []
        for v, g in groupby(row):
            if v == "#":
                seq.append(len(list(g)))

        if seq == vals:
            ans += 1

print(ans)


"""
PART I and II fast
"""


@lru_cache(maxsize=None)
def check_combinations(row: str, vals: tuple[int], in_sequence: bool = False) -> int:
    """
    Recursive function to check all possible combinations of # and . in a row.
    The idea is to recursively check each possible character if it is possible
    For example on a sequence of #, if value is 0, then we need to continue with a . to break the sequence

    Example:
    0. row = "??#.#" and vals = (3, 1)

    the first case we will try both meaning

    1. row = "#?#.#" and vals = (2, 1)
    2. row = ".?#.#" and vals = (3, 1)
              ^

    Then at iteration 2, we will have

    1.1 row = "#.#.#" <- This one makes no sense as we are in a sequence and vals[0] > 0
    1.2 row = "###.#" and vals = (1, 1)
                ^
    2.1 row = "..#.#" and vals = (3, 1)
    2.2 row = ".##.#" and vals = (2, 1)
                ^

    Then at iteration 3, we will have only a filtering as it is not a ?

    1.2.1 row = "###.#" and vals = (0, 1)  <- we have -1 as there is an #
    2.1.1 row = "..#.#" and vals = (2, 1)
    2.2.1 row = ".##.#" and vals = (1, 1)
                   ^

    Then at iteration 4, 2.1.1 and 2.2.1 will be invalid as we exit the sequence vals[0] > 0
    So this will continue only with 1.2.1 to the end of the row leading to 1 valid combination only

    row (str): the row to check for example "??.#.#"
    vals (tuple[int]): the number of # to place in the row for example (2, 1, 1)
    in_sequence (bool): whether the sequence is currently in a sequence of # or not
    """

    if len(row) == 0:  # end of row
        return int(sum(vals) == 0)  # if all vals have been used so the combination is valid

    if sum(vals) == 0:  # no more # available
        return int("#" not in row)  # this combination is invalid if there is still a # in the row

    actual_char, next_chars = row[0], row[1:]
    actual_value, next_values = vals[0], vals[1:]

    decremented_vals = (actual_value - 1, *next_values)

    if actual_char == "#":
        if in_sequence and actual_value == 0:
            # invalid combination because there is no # left for this sequence
            return 0
        else:
            # we continue with the next char and 1 less # possible
            return check_combinations(next_chars, decremented_vals, in_sequence=True)
    elif actual_char == ".":
        if in_sequence and actual_value > 0:
            # the sequence is broken but we still need some #
            return 0
        elif actual_value == 0:
            # we continue with the next char but now the sequence is broken
            # that's why we have now next_values
            return check_combinations(next_chars, next_values, in_sequence=False)
        else:
            # we simply continue with the next char as we were out of sequence with a .
            return check_combinations(next_chars, vals, in_sequence=False)
    else:  # actual_char == "?"
        if in_sequence and actual_value == 0:
            # in that case, we need to use a . to break the sequence as there is no remaining #
            return check_combinations(next_chars, next_values, in_sequence=False)
        elif in_sequence:
            # otherwise we need to continue the sequence with a # otherwise the pattern is broken as actual_value > 0
            return check_combinations(next_chars, decremented_vals, in_sequence=True)
        else:
            # if we are out of sequence, we can either continue with a # or a .
            return (
                check_combinations(next_chars, vals, in_sequence=False) +
                check_combinations(next_chars, decremented_vals, in_sequence=True)
            )


VERSION = 1

with open('input12.txt') as f:
    lines = [x.replace("\n", "") for x in f.readlines()]

tic = time.time()
ans = 0
for line in lines:
    row, vals = line.split()
    nums = tuple(int(x) for x in vals.split(","))  # require tuple for the lru_cache as list is not hashable
    if VERSION == 2:
        row = "?".join([row for _ in range(5)])
        nums = tuple(nums * 5)  # require tuple for the lru_cache as list is not hashable
    ans += check_combinations(row, nums)
toc = time.time()
print(ans)

print(toc - tic)  # 0.9309 for part 2
print(check_combinations.cache_info())  # CacheInfo(hits=125825, misses=695275, maxsize=None, currsize=695275)
