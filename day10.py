from collections import deque
from shapely.geometry import Polygon, Point


def get_border(grid: list[str], start: tuple[int, int], W: int, H: int) -> tuple[set[tuple[int, int]], str]:
    """
    Use a BFS to find the border of the maze.
    At the same time, we can find the closing character of the maze to replace S
    """
    border = set()
    Q = deque([start])

    from_south = {"|", "┐", "┌"}
    from_north = {"|", "┘", "└"}
    from_west = {"-", "┘", "┐"}
    from_east = {"-", "└", "┌"}
    start = {"S"}
    all_possible_closing_chars = from_south | from_north | from_west | from_east

    dirs = [
        (0, 1, from_east, from_west),
        (0, -1, from_west, from_east),
        (1, 0, from_south, from_north),
        (-1, 0, from_north, from_south)
    ]

    while Q:
        row, col = Q.popleft()

        border.add((row, col))

        for drow, dcol, entry, exit in dirs:
            if (
                (0 <= row + drow < H) and
                (0 <= col + dcol < W) and
                (grid[row][col] in (start | entry)) and
                (grid[row + drow][col + dcol] in exit) and
                ((row + drow, col + dcol) not in border)
            ):
                Q.append((row + drow, col + dcol))
                if grid[row][col] in start:
                    all_possible_closing_chars &= entry

    closing_char = all_possible_closing_chars.pop()  # There should be only one normally

    return border, closing_char


def get_polygon(grid: list[list[str]], border: set[tuple[int, int]]) -> Polygon:
    """
    Order the border of the maze
    """
    G = {
        "|": {
            "U": "D",
            "D": "U"
        },
        "┐": {
            "L": "D",
            "D": "L"
        },
        "┌": {
            "R": "D",
            "D": "R"
        },
        "┘": {
            "L": "U",
            "U": "L"
        },
        "└": {
            "R": "U",
            "U": "R"
        },
        "-": {
            "L": "R",
            "R": "L"
        }
    }

    I = {
        "U": "D",
        "D": "U",
        "L": "R",
        "R": "L"
    }

    row, col = border.pop()

    item = grid[row][col]
    in_dir = list(G[item].keys())[0]

    ans = [(row, col)]

    while True:
        item = grid[row][col]
        out_dir = G[item][in_dir]
        if out_dir == "U":
            row -= 1
        elif out_dir == "D":
            row += 1
        elif out_dir == "L":
            col -= 1
        elif out_dir == "R":
            col += 1
        
        in_dir = I[out_dir]
        ans.append((row, col))

        if (row, col) == ans[0]:
            break

    return Polygon(ans)


def get_outside_positions(grid: list[str], start: tuple[int, int], W: int, H: int) -> set[tuple[int, int]]:
    """
    Use a BFS to find the outside positions of the maze
    The start point in 0, 0 which is always outside thanks to the scaling
    """
    Q = deque([start])
    visited = set()

    while Q:
        row, col = Q.popleft()

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for drow, dcol in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            trow, tcol = row + drow, col + dcol
            if (
                (0 <= trow < H) and
                (0 <= tcol < W) and
                (grid[trow][tcol] == ".")
            ):
                Q.append((trow, tcol))

    return visited


def scale(grid: list[str]) -> list[str]:
    """
    Scale the grid by 3 times to find inner dots
    For example └ becosmes

    .|.
    .└-
    ...
    """
    ans = []
    for row in grid:

        # First row of the scaled grid
        s = ""
        for char in row:
            if char in "┌┐.-":
                s += "..."
            elif char in "└┘|":
                s += ".|."
        ans.append(s)

        # Second row of the scaled grid
        s = ""
        for char in row:
            if char in "-":
                s += "---"
            elif char in "└":
                s += ".└-"
            elif char in "┘":
                s += "-┘."
            elif char in "┌":
                s += ".┌-"
            elif char in "┐":
                s += "-┐."
            elif char in "|":
                s += ".|."
            elif char in ".":
                s += "..."
        ans.append(s)

        # Third row of the scaled grid
        s = ""
        for char in row:
            if char in "┌┐|":
                s += ".|."
            elif char in "└┘.-":
                s += "..."
        ans.append(s)

    return ans


with open('input10.txt') as f:
    lines = [
        x
        .replace("\n", "")
        .replace("J", "┘")
        .replace("7", "┐")
        .replace("L", "└")
        .replace("F", "┌")
        for x in f.readlines()
    ]

# print(*lines, sep="\n")

W = len(lines[0])
H = len(lines)

# print(*lines, sep="\n")

for i, line in enumerate(lines):
    if "S" in line:
        start = (i, line.index("S"))
        break

borders, closing_char = get_border(lines, start, W, H)

lines[start[0]] = lines[start[0]].replace("S", closing_char)
clean_grid = [[char if (i, j) in borders else "." for j, char in enumerate(row)] for i, row in enumerate(lines)]


# Solution 1 - Using BFS

# print(*["".join(row) for row in clean_grid], sep="\n")

clean_grid = scale(clean_grid)

# print(*["".join(row) for row in clean_grid], sep="\n")

W2 = len(clean_grid[0])
H2 = len(clean_grid)

outside = get_outside_positions(clean_grid, (0, 0), W2, H2)

filled_grid = []
for i, row in enumerate(clean_grid):
    s = "".join(char if (i, j) not in outside else "#" for j, char in enumerate(row)) 
    filled_grid.append(s)
    # print(s)

# the remaining dots are the ones inside the maze
# but we need only to count the ones from an initial . which means it's a . in the middle of the 3x3 grid
dots = 0
for i in range(1, len(filled_grid), 3):
    for j in range(1, len(filled_grid[0]), 3):
        if filled_grid[i][j] == ".":
            dots += 1

for row in filled_grid[1::3]:
    print(row[1::3])

print(len(borders) // 2)
print(dots)


# Solution 2 - Using Shapely
poly = get_polygon(clean_grid, borders)
ans = 0
for i in range(H):
    for j in range(W):
        if clean_grid[i][j] == ".":
            pt = Point(i, j)
            ans += poly.contains(pt)
print(ans)
