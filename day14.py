import time
import numpy as np

"""
This solution is quite slow and requires improvements for applying gravity and maybe the hash function.
"""


def apply_gravity_up(matrix):
    """
    Shift all 1s in the matrix upwards until they reach a 0 or 2 (or a previous 1).
    """
    rows, cols = matrix.shape

    for col in range(cols):
        up = 0
        for down in range(1, rows):
            if matrix[down, col] == 2:
                up = down + 1
            elif matrix[up, col] > 0:
                up += 1
            elif matrix[up, col] == 0 and matrix[down, col] == 1:
                matrix[up, col], matrix[down, col] = matrix[down, col], matrix[up, col]
                up += 1

    return matrix


def hash_matrix(matrix):
    """
    Returned a hashed version of the matrix.
    """
    return hash(matrix.tobytes())


def cycle(matrix):
    """
    Apply a cycle of gravity to the matrix.
    """
    for _ in range(4):
        matrix = apply_gravity_up(matrix)
        matrix = np.rot90(matrix, k=-1)
    return matrix


def score(matrix):
    """
    Compute the score of the matrix.
    """
    H, W = matrix.shape
    ans = 0
    for i in range(H):
        ans += (H-i) * len(np.where(matrix[i] == 1)[0])

    return ans


with open('input14.txt') as f:
    lines = f.readlines()

VERSION = 2
mapping = {".": 0, "#": 2, "O": 1}

grid = np.array([[mapping[x] for x in line if x != "\n"] for line in lines])

tic = time.time()
if VERSION == 1:
    grid = apply_gravity_up(grid)
    print(score(grid))

elif VERSION == 2:

    init_hash = hash_matrix(grid)

    hashlist = [init_hash]
    hashmap = {init_hash: grid.copy()}

    while True:
        grid = cycle(grid)
        h = hash_matrix(grid)
        if h in hashlist:
            break
        hashlist.append(h)
        hashmap[h] = grid.copy()

    first_match = hashlist.index(h)
    current_turn = len(hashlist)
    cycle_length = current_turn - first_match

    iteration = (1_000_000_000 - first_match) % cycle_length + first_match
    resulting_hash = hashlist[iteration]
    resulting_grid = hashmap[resulting_hash]

    print(score(resulting_grid))
