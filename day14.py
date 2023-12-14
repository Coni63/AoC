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
        # Get the indices of 1s in the current column
        ones_indices = np.where(matrix[:, col] == 1)[0]

        # Iterate through each 1 in the current column
        for idx in ones_indices:
            # Move the 1 upwards until it reaches a 0 or 2
            while idx > 0 and matrix[idx - 1, col] == 0:
                matrix[idx, col], matrix[idx - 1, col] = matrix[idx - 1, col], matrix[idx, col]
                idx -= 1

    return matrix


def apply_gravity(matrix, direction):
    """
    Apply gravity to the matrix in the given direction (up, down, left, right).
    """
    if direction == "up":
        return apply_gravity_up(matrix)
    elif direction == "down":
        matrix = np.rot90(matrix, k=2)
        matrix = apply_gravity_up(matrix)
        matrix = np.rot90(matrix, k=2)
        return matrix
    elif direction == "right":
        matrix = np.rot90(matrix, k=1)
        matrix = apply_gravity_up(matrix)
        matrix = np.rot90(matrix, k=3)
        return matrix
    elif direction == "left":
        matrix = np.rot90(matrix, k=3)
        matrix = apply_gravity_up(matrix)
        matrix = np.rot90(matrix, k=1)
        return matrix


def hash_matrix(matrix):
    """
    Returned a hashed version of the matrix.
    """
    return "".join(str(x) for x in matrix.flatten())


def cycle(matrix):
    """
    Apply a cycle of gravity to the matrix.
    """
    matrix = apply_gravity(matrix, direction="up")
    matrix = apply_gravity(matrix, direction="left")
    matrix = apply_gravity(matrix, direction="down")
    matrix = apply_gravity(matrix, direction="right")
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
    grid = apply_gravity(grid, direction="up")
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

print(time.time() - tic)