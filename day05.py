def get_next_range(source: list[list[int]], ranges: list[list[int]]) -> list[list[int]]:
    """
    Project each source range (x_start, e_end) onto the target ranges (y_start, y_end)
    Those new ranges are the new source ranges (x_start, x_end) for the next projection
    In case of overlap, split the source range into two or three parts.
    """
    target = []
    for start, end in source:
        for init_y, init_x, range_width in ranges:
            # check if there is overlap and split if needed
            new_start = max(start, init_x)
            new_end = min(end, init_x + range_width - 1)
            if new_start <= new_end:  # means overlap exists
                target.append((new_start - init_x + init_y, new_end - init_x + init_y))
                if new_start > start:
                    target.append((start, new_start - 1))
                if new_end < end:
                    target.append((new_end + 1, end))
                break
        else:  # no overlap found in any range (for-else loop, not if-else)
            target.append((start, end))
    return target


def parse_stage(stage: str) -> list[list[int]]:
    """
    Parse a section of the input into a list of ranges
    """
    ranges = []
    for section in stage.split("\n")[1:]:
        y, x, z = [int(x) for x in section.split()]
        ranges.append((y, x, z))
    return ranges


def parse_seed(seed: str, version=1) -> list[list[int]]:
    """
    Process the seed row into a list of ranges (start, end) instead of (start, offset)
    """
    if version == 1:
        init_seeds = []
        for x in seed[7:].split():
            init_seeds.extend([int(x), 1])
    else:
        init_seeds = [int(x) for x in lines[0][7:].split()]

    ranges = []
    for seed_start, seed_offset in zip(init_seeds[::2], init_seeds[1::2]):
        ranges.append((seed_start, seed_start + seed_offset - 1))
    return ranges


if __name__ == "__main__":
    with open("input05.txt", "r") as f:
        lines = f.read().split("\n\n")

    source = parse_seed(lines[0], version=1)
    # print(source)

    for stage in lines[1:]:
        ranges = parse_stage(stage)
        source = get_next_range(source, ranges)
        # print(source)

    print(min([x[0] for x in source]))
