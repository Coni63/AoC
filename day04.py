import re


def str_to_num(s):
    nums = re.sub("[^0-9 ]", "", s).strip().split(" ")
    nums = [int(x) for x in nums if x.isnumeric()]
    return nums


def solve(version):
    with open("input04.txt", "r") as f:
        lines = f.readlines()

    lines = [x.replace("\n", "") for x in lines]

    ans = 0
    matches = []
    for line in lines:
        before, after = line.split("|")
        before = before.split(":")[1].strip()

        cards, winner = str_to_num(before), str_to_num(after)
        common = set(cards).intersection(set(winner))

        matches.append(len(common))

        # V1
        if len(common) > 0:
            ans += 2**(len(common) - 1)
    print(ans)

    if version == 1:
        return

    copies = [1 for _ in range(len(lines))]
    for i, match in enumerate(matches):
        if copies[i] == 0:
            break

        for j in range(i+1, i+match+1):
            copies[j] += copies[i]

    print(sum(copies))


if __name__ == "__main__":
    solve(1)
    solve(2)
