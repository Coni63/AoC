import numpy as np


def find_symetry(g):
    H, W = g.shape

    for i in range(W-1):
        offset = 0
        while True:
            if (i-offset) < 0 or (i+offset+1) >= W:
                return i+1
            if np.array_equal(g[:, i-offset], g[:, i+offset+1]):
                offset += 1
            else:
                break

    return 0


with open('input13.txt') as f:
    puzzles = f.read().split("\n\n")

ans = 0
for puzzle in puzzles:
    g = np.array([[1 if x == "#" else 0 for x in row] for row in puzzle.split("\n")])

    # print(g)

    a = find_symetry(g)
    b = find_symetry(g.T)

    ans += a + 100 * b

    # print(g.shape)
    # print(a, b)

print(ans)