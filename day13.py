import numpy as np


def find_symetry(g: list[list[int]], accepted_errors: int) -> int:
    """
    Return the vertical index of a mirror
    Index starts at 1 but return 0 if no mirror
    """
    H, W = g.shape

    for col in range(1, W):
        max_width = min(col, W-col)

        start = col-max_width
        mid = col
        end = col+max_width

        C1 = g[:, start:mid]
        C2 = np.fliplr(g[:, mid:end])

        mismatch = np.abs(C1 - C2).sum()

        if mismatch == accepted_errors:
            return col

    return 0


with open('input13.txt') as f:
    puzzles = f.read().split("\n\n")

VERSION = 1
ans = 0

errors = 0 if VERSION == 1 else 1
for puzzle in puzzles:
    g = np.array([[1 if x == "#" else 0 for x in row] for row in puzzle.split("\n")])

    ans += find_symetry(g, accepted_errors=errors)
    ans += 100 * find_symetry(g.T, accepted_errors=errors)

print(ans)
