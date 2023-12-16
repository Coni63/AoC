import math


def get_graph(lines):
    """
    Build a graph from the input lines
    """
    graph = {}
    for line in lines:
        node, targets = line.split("=")
        node = node.strip()
        left, right = [x.strip() for x in targets.strip()[1:-1].split(",")]
        graph[node] = (left, right)
    return graph


def get_step(node, end_nodes, dirs, graph, N):
    """
    Count the number of steps to reach one of the end nodes knowing the graph and the directions
    """
    ans = 0
    while True:
        i = dirs[ans % N]
        if node in end_nodes:
            return ans
        ans += 1
        node = graph[node][i]


def solve(version):

    with open('input08.txt') as f:
        lines = f.readlines()

    directions = lines[0].strip()
    dir_index = [0 if x == "L" else 1 for x in directions]

    N = len(directions)

    network = get_graph(lines[2:])

    if version == 1:
        current = ["AAA"]
        ends = ["ZZZ"]
    else:
        current = [x for x in network if x.endswith("A")]
        ends = [x for x in network if x.endswith("Z")]

    cycle_size = [get_step(node, ends, dir_index, network, N) for node in current]

    lcm = 1  # least common multiple
    for i in cycle_size:
        lcm = lcm*i//math.gcd(lcm, i)
    print(lcm)


if __name__ == "__main__":
    solve(1)
    solve(2)
