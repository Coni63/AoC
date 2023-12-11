import numpy as np

with open('input11.txt') as f:
    lines = f.readlines()

lines = [line.replace("\n", "") for line in lines]

grid = np.array([[1 if char == "#" else 0 for char in line] for line in lines])

empty_rows = np.argwhere(grid.sum(axis=1) == 0).flatten().tolist()
empty_cols = np.argwhere(grid.sum(axis=0) == 0).flatten().tolist()
stars = np.argwhere(grid == 1).tolist()

ans = 0
K = 1000000

for i, (r1, c1) in enumerate(stars):
    for (r2, c2) in stars[:i]:
        x_start = min(c1, c2)
        x_end = max(c1, c2)
        y_start = min(r1, r2)
        y_end = max(r1, r2)
        ans += sum([1, K][x in empty_cols] for x in range(x_start, x_end))
        ans += sum([1, K][y in empty_rows] for y in range(y_start, y_end))

print(ans)
