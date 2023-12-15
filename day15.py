def get_hash(word):
    ans = 0
    for letter in word:
        ans += ord(letter)
        ans *= 17
        ans %= 256
    return ans


with open('input15.txt') as f:
    lines = f.read().split(",")

VERSION = 1

if VERSION == 1:
    print(sum(map(get_hash, lines)))

else:
    boxes = [[] for _ in range(256)]
    lenses = {}

    for line in lines:
        if "=" in line:
            label, focal = line.split("=")
            idx = get_hash(label)
            focal = int(focal)
            lenses[label] = focal
            if label not in boxes[idx]:
                boxes[idx].append(label)
        elif "-" in line:
            label = line[:-1]
            index = get_hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)

    total = 0

    for box_idx, box_list in enumerate(boxes, start=1):
        for lens_idx, lens_label in enumerate(box_list, start=1):
            total += box_idx * lens_idx * lenses[lens_label]

    print(total)