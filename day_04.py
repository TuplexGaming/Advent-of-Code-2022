from aocd import get_data


def get_input(day, year=2022):
    data = get_data(day=day, year=year)
    pairs_raw = data.splitlines()
    pairs = []
    for pair_raw in pairs_raw:
        pair = pair_raw.split(',')
        for p in pair:
            pairs.append([int(r) for r in p.split('-')])
    return pairs


def part_1():
    pairs = get_input(4)
    count = 0
    for i in range(0, len(pairs), 2):
        elf_a = range(pairs[i][0], pairs[i][1] + 1)
        elf_b = range(pairs[i+1][0], pairs[i+1][1] + 1)
        if set(elf_a).issubset(elf_b) or set(elf_b).issubset(elf_a):
            count += 1
    return count


def part_2():
    pairs = get_input(4)
    # pairs =[
    #     [2, 4], [6, 8],
    #     [2, 3], [4, 5],
    #     [5, 7], [7, 9],
    #     [2, 8], [3, 7],
    #     [6, 6], [4, 6],
    #     [2, 6], [4, 8]
    # ]


if __name__ == "__main__":
    print("Part 1: ", part_1())
    print("Part 2: ", part_2())
