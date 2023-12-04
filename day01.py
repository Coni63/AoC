letters = {
    # "one": 1,
    # "two": 2,
    # "three": 3,
    # "four": 4,
    # "five": 5,
    # "six": 6,
    # "seven": 7,
    # "eight": 8,
    # "nine": 9,
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


def find_first_value(word):
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


def find_last_value(word):
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


total = 0
with open('input01.txt') as f:
    for line in f:
        total += find_first_value(line) * 10 + find_last_value(line)
print(total)
