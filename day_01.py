def get_input():
    with open("./inputs/day_01.txt") as file:
        return file.readlines()


def part_1():
    max_calories = 0
    current_calories = 0
    data = get_input()
    for line in data:
        if line != "\n":
            current_calories += int(line)
        else:
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
    return max_calories


def part_2():
    top_3 = [0, 0, 0]
    current_calories = 0
    data = get_input()
    for line in data:
        if line != "\n":
            current_calories += int(line)
        else:
            top_3.append(current_calories)
            top_3.sort(reverse=True)
            top_3.pop()
            current_calories = 0
    return sum(top_3)


if __name__ == "__main__":
    print("Part 1: ", part_1())
    print("Part 2: ", part_2())
