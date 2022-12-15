test_data = ["A Y", "B X", "C Z"]
outcomes = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3},
}
choices = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"},
}
scores = {"X": 1, "Y": 2, "Z": 3}


def get_input():
    with open("./inputs/day_02.txt") as file:
        return file.readlines()


def part_1():
    total_score = 0
    for round in get_input():
        elf, me = round.strip().split(" ")
        outcome = outcomes[me][elf]
        score = scores[me]
        total_score += outcome + score
    return total_score


def part_2():
    total_score = 0
    for round in get_input():
        elf, outcome = round.strip().split(" ")
        me = choices[elf][outcome]
        outcome = outcomes[me][elf]
        score = scores[me]
        total_score += outcome + score
    return total_score


if __name__ == "__main__":
    print("Part 1: ", part_1())
    print("Part 2: ", part_2())
