import heapq


def get_minimum_loss(grid, min_step, max_step):
    directions = [
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 0)
    ]

    H, W = len(grid), len(grid[0])

    q = []
    visited = set()   # (row, col, direction, current_step) -> distance

    heapq.heappush(q, (0, 0, 0, 0, 0))  # horizontal entry format (distance, row, col, direction, current_step)
    heapq.heappush(q, (0, 0, 0, 3, 0))  # vertical entry

    ans = float('inf')

    while q:
        distance, row, col, direction_idx, current_step = heapq.heappop(q)
        if (row, col, direction_idx, current_step) in visited:
            continue

        visited.add((row, col, direction_idx, current_step))

        if row == H-1 and col == W-1:
            ans = min(ans, distance)
        
        if current_step < max_step:
            # keep going straight
            row2 = row + directions[direction_idx][0]
            col2 = col + directions[direction_idx][1]
            
            if row2 < 0 or row2 >= H or col2 < 0 or col2 >= W:
                pass
            else:
                heapq.heappush(q, (grid[row2][col2] + distance, row2, col2, direction_idx, current_step + 1))
            
        if current_step >= min_step:
            # change direction
            direction1_idx = (direction_idx + 3) % 4
            row2 = row + directions[direction1_idx][0]
            col2 = col + directions[direction1_idx][1]

            if row2 < 0 or row2 >= H or col2 < 0 or col2 >= W:
                pass
            else:
                heapq.heappush(q, (grid[row2][col2] + distance, row2, col2, direction1_idx, 1))

            # change direction 2
            direction1_idx = (direction_idx + 5) % 4
            row2 = row + directions[direction1_idx][0]
            col2 = col + directions[direction1_idx][1]

            if row2 < 0 or row2 >= H or col2 < 0 or col2 >= W:
                pass
            else:
                heapq.heappush(q, (grid[row2][col2] + distance, row2, col2, direction1_idx, 1))

    return ans


def solve(version):
    with open('input17.txt') as f:
        grid = [[int(x) for x in line if x != "\n"] for line in f]

    if version == 1:
        print(get_minimum_loss(grid, 0, 3))
    else:
        print(get_minimum_loss(grid, 4, 10))


if __name__ == '__main__':
    solve(1)
    solve(2)
