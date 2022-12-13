def part1(file):
    return max(sum(foods) for foods in foods_per_elf(file))


def part2(file):
    calories_per_elf = sorted([sum(foods) for foods in foods_per_elf(file)], reverse=True)
    return sum(calories_per_elf[0:3])


def foods_per_elf(file):
    calories = []
    for line in file:
        if line == '':
            yield calories
            calories = []
            continue
        calories.append(int(line))
    yield calories
