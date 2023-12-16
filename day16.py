from collections import deque


def get_visited_cells(grid, entry):
    W = len(grid[0])
    H = len(grid)

    visited = {entry}
    Q = deque([entry])

    while Q:
        row, col, drow, dcol = Q.popleft()

        if row < 0 or row >= H or col < 0 or col >= W:
            continue

        visited.add((row, col, drow, dcol))

        char = grid[row][col]

        if char == ".":
            next_entries = [(row+drow, col+dcol, drow, dcol)]
        elif char == "/":
            next_entries = [(row-dcol, col-drow, -dcol, -drow)]
        elif char == "\\":
            next_entries = [(row+dcol, col+drow, dcol, drow)]
        elif char == "-":
            if dcol != 0:
                next_entries = [(row+drow, col+dcol, drow, dcol)]
            else:
                next_entries = [(row, col+1, 0, 1), (row, col-1, 0, -1)]
        elif char == "|":
            if drow != 0:
                next_entries = [(row+drow, col+dcol, drow, dcol)]
            else:
                next_entries = [(row+1, col, 1, 0), (row-1, col, -1, 0)]

        for next_entry in next_entries:
            if next_entry not in visited:
                Q.append(next_entry)

    return len({(r, c) for (r, c, *_) in visited})


def solve(version):
    with open('input16.txt') as f:
        grid = f.read().splitlines()

    if version == 1:
        print(get_visited_cells(grid, (0, 0, 0, 1)))
    else:
        ans = 0
        for row in range(len(grid)):
            ans = max(ans, get_visited_cells(grid, (row,  0, 0,  1)))
            ans = max(ans, get_visited_cells(grid, (row, -1, 0, -1)))

        for col in range(len(grid[0])):
            ans = max(ans, get_visited_cells(grid, (0, col,  1, 0)))
            ans = max(ans, get_visited_cells(grid, (-1, col, -1, 0)))

        print(ans)


if __name__ == "__main__":
    solve(1)
    solve(2)