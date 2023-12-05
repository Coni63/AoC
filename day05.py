def get_next_range(source, ranges):
    ans = []
    for start, end in source:
        for y, x, z in ranges:
            # check if there is overlap and split if needed
            new_start = max(start, x)
            new_end = min(end, x + z - 1)
            if new_start <= new_end:
                ans.append((new_start - x + y, new_end - x + y))
                if new_start > start:
                    ans.append((start, new_start - 1))
                if new_end < end:
                    ans.append((new_end + 1, end))
                break
        else:
            ans.append((start, end))
    return ans


def parse_stage(stage):
    sections = stage.split("\n")[1:]
    ranges = []
    for section in sections:
        y, x, z = [int(x) for x in section.split()]
        ranges.append((y, x, z))
    return ranges


def parse_seed(seed, version=1):
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

    source = parse_seed(lines[0], version=2)
    # print(source)

    for stage in lines[1:]:
        # print(source)
        ranges = parse_stage(stage)
        source = get_next_range(source, ranges)

    print(min([x[0] for x in source]))
