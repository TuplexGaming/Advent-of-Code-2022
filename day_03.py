import string


priority = string.ascii_letters

test_data = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def get_input(filename):
    with open(filename) as file:
        return file.readlines()


def part_1():
    sum = 0
    for rucksack in get_input("./inputs/day_03.txt"):
        rucksack = rucksack.strip()
        comp1 = rucksack[: len(rucksack) // 2]
        comp2 = rucksack[len(rucksack) // 2 :]
        for item in comp1:
            if item in comp2:
                common_item = item
                break
        sum += priority.index(common_item) + 1
    return sum


def part_2():
    sum = 0
    data = get_input("./inputs/day_03.txt")
    for i in range(0, len(data), 3):
        rucksacks = data[i : i + 3]
        rucksacks.sort(key=len)
        for item in rucksacks[0]:
            if item in rucksacks[1] and item in rucksacks[2]:
                common_item = item
                break
        sum += priority.index(common_item[0]) + 1
    return sum


if __name__ == "__main__":
    print("Part 1: ", part_1())  # 7716
    print("Part 2: ", part_2())  # 2973
