import operator
from pydantic import BaseModel
from functools import reduce


class Number(BaseModel):
    value: int = 0
    row: int
    x_start: int
    x_end: int

    def get_neighbors(self, W, H):
        ans = []
        for col in range(self.x_start, self.x_end+1):
            if in_grid(self.row-1, col, W, H):
                ans.append([self.row-1, col])

            if in_grid(self.row+1, col, W, H):
                ans.append([self.row+1, col])

        for r in range(self.row-1, self.row+2):
            if in_grid(r, self.x_start-1, W, H):
                ans.append([r, self.x_start-1])

            if in_grid(r, self.x_end+1, W, H):
                ans.append([r, self.x_end+1])

        return ans

    def get_positions(self):
        return [[self.row, col] for col in range(self.x_start, self.x_end+1)]


class Symbol(BaseModel):
    symbol: str
    row: int
    col: int

    def get_positions(self):
        return [[self.row, self.col]]

    def get_neighbors(self, W, H):
        adjacents = [
            [self.row-1, self.col],
            [self.row+1, self.col],
            [self.row, self.col-1],
            [self.row, self.col+1],
            [self.row-1, self.col-1],
            [self.row-1, self.col+1],
            [self.row+1, self.col-1],
            [self.row+1, self.col+1],
        ]

        return [x for x in adjacents if in_grid(*x, W, H)]


def in_grid(row, col, W, H):
    return row >= 0 and row < H and col >= 0 and col < W


def to_hash(row, col):
    return 10000 * row + col


def solve(version):
    with open('input03.txt') as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]
    W = len(lines[0])
    H = len(lines)

    all_chars = set()
    for line in lines:
        all_chars |= set(line)
    all_chars -= {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", "."}

    numbers = []
    symbols = []
    for i, line in enumerate(lines):
        number = None
        for j, char in enumerate(line):
            if char.isnumeric() and number is None:
                number = Number(row=i, x_start=j, x_end=j)
                numbers.append(number)
            elif char.isnumeric() and number is not None:
                number.x_end = j
            else:
                number = None
                if char in all_chars:
                    symbols.append(Symbol(symbol=char, row=i, col=j))

    for number in numbers:
        number.value = int(lines[number.row][number.x_start:number.x_end+1])

    symbols_hash = {to_hash(row, col): i for i, symbol in enumerate(symbols) for row, col in symbol.get_positions()}
    numbers_hash = {to_hash(row, col): i for i, number in enumerate(numbers) for row, col in number.get_positions()}

    if version == 1:
        ans = 0
        for number in numbers:
            for row, col in number.get_neighbors(W, H):
                if to_hash(row, col) in symbols_hash:
                    ans += number.value
                    break
        print(ans)

    else:
        ans2 = 0
        for symbol in symbols:
            adjacent_numbers = set()
            for row, col in symbol.get_neighbors(W, H):
                if to_hash(row, col) in numbers_hash:
                    adjacent_numbers.add(numbers_hash[to_hash(row, col)])
            if len(adjacent_numbers) > 1:
                ans2 += reduce(operator.mul, [numbers[i].value for i in adjacent_numbers], 1)
        print(ans2)


if __name__ == "__main__":
    solve(1)
    solve(2)
