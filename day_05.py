from aocd import get_data


def get_input(day, year=2022):
    stacks = [
        ['Z', 'J', 'G'],
        ['Q', 'L', 'R', 'P', 'W', 'F', 'V', 'C'],
        ['F', 'P', 'M', 'C', 'L', 'G', 'R'],
        ['L', 'F', 'B', 'W', 'P', 'H', 'M'],
        ['G', 'C', 'F', 'S', 'V', 'Q'],
        ['W', 'H', 'J', 'Z', 'M', 'Q', 'T', 'L'],
        ['H', 'F', 'S', 'B', 'V'],
        ['F', 'J', 'Z', 'S'],
        ['M', 'C', 'D', 'P', 'F', 'H', 'B', 'T']
    ]
    data = get_data(day=day, year=year)
    instructions = data.splitlines()[10:]
    return stacks, instructions


def parse_instruction(instruction):
    i = instruction.split(" ")
    return [int(i[1]), int(i[3]) - 1, int(i[5]) - 1]


def part_1():
    stacks, instructions = get_input(5)
    for instruction in instructions:
        qty, stack_from, stack_to = parse_instruction(instruction)
        for _ in range(qty):
            stacks[stack_to].append(stacks[stack_from].pop())
    return "".join([stack[-1] for stack in stacks])


def part_2():
    stacks, instructions = get_input(5)
    for instruction in instructions:
        qty, stack_from, stack_to = parse_instruction(instruction)
        move_stack = stacks[stack_from][-qty:]
        stacks[stack_from] = stacks[stack_from][0: -qty]
        stacks[stack_to] += move_stack
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    print("Part 1: ", part_1())
    print("Part 2: ", part_2())
