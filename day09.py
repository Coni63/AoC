def reduce(array, version=1):
    if sum(array) == 0:
        return 0

    diff = reduce(
        [y - x for x, y in zip(array[:-1], array[1:])], 
        version=version
    )

    return array[0] - diff if version == 2 else array[-1] + diff


with open('input09.txt') as f:
    lines = f.readlines()

VERSION = 2
ans = 0

for line in lines:
    nums = [int(x) for x in line.split()]
    ans += reduce(nums, version=VERSION)

print(ans)
