

def find_first_value(word, letters):
    lowest_index = len(word)
    value = 0
    for option in letters:
        idx = word.find(option)
        if idx == -1:
            continue

        if idx < lowest_index:
            lowest_index = idx
            value = letters[option]

    return value


def find_last_value(word, letters):
    highest_index = -1
    value = 0
    for option in letters:
        idx = word.rfind(option)
        if idx == -1:
            continue

        if idx > highest_index:
            highest_index = idx
            value = letters[option]

    return value


def solve(version):
    if version == 1:
        letters = {
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
    else:
        letters = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
    total = 0
    with open('input01.txt') as f:
        for line in f:
            total += find_first_value(line, letters) * 10 + find_last_value(line, letters)
    print(total)


if __name__ == "__main__":
    solve(1)
    solve(2)
