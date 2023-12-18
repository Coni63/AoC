from shapely.geometry import Polygon


def get_dist_dir(s, version):
    d, n, color = s.replace("\n", "").split(" ")
    if version == 1:
        return int(n), d
    else:
        return int(color[2:-2], 16), "RDLU"[int(color[-2])]


def solve(version):
    dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    with open('input18.txt') as f:

        point = (0, 0)
        points = [point]

        for line in f:
            dist, direction = get_dist_dir(line, version)
            drow, dcol = dirs[direction]
            point = (point[0] + drow * dist, point[1] + dcol * dist)

            points.append(point)

        p = Polygon(points)

        return p.area + p.length // 2 + 1



if __name__ == "__main__":
    print(solve(1))
    print(solve(2))