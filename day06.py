import math


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def read_input(lines, version=1):
    if version == 1:
        times = [int(x) for x in lines[0].split(":")[1].split()]
        distances = [int(x) for x in lines[1].split(":")[1].split()]
        return times, distances
    else:
        times = [int(lines[0].split(":")[1].replace(" ", "").replace("\n", ""))]
        distances = [int(lines[1].split(":")[1].replace(" ", "").replace("\n", ""))]
        return times, distances
    

def solve(version):
    with open('input06.txt') as f:
        lines = f.readlines()

    times, distances = read_input(lines, version=2)

    if version == 1:
        ans = 1
        for time, distance in zip(times, distances):
            ans *= sum((time * hold) - (hold**2) > distance for hold in range(time))

        print(ans)
    else:
        ans = 1
        for time, distance in zip(times, distances):
            a, b, c = -1, time, -distance
            delta = b**2 - 4*a*c
            r1 = (-b + delta**0.5) / (2*a)  # 0 < r1 < r2 < ???
            r2 = (-b - delta**0.5) / (2*a)
            t1 = clamp(math.ceil(r1), 0, time)  # take the first next integer as the start time cannot be float
            t2 = clamp(math.floor(r2), 0, time)  # take the last previous integer as the end time cannot be float
            ans *= t2-t1+1
        print(ans)


if __name__ == "__main__":
    solve(1)
    solve(2)
