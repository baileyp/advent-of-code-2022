from functools import reduce


def part1(file):
    return sum(item_to_priority(matching_item(line_to_sack(line))) for line in file)


def part2(file):
    return sum(item_to_priority(matching_item(group)) for group in elves_from_file(file))


def line_to_sack(line):
    half = int(len(line) / 2)
    return [set(line[0:half]), set(line[half:])]


def matching_item(grouped_items):
    return reduce(lambda a, b: a & b, grouped_items).pop()


def item_to_priority(item):
    priority = ord(item) - 38
    return priority if priority < 53 else priority - 58


def elves_from_file(file):
    group = []
    for line in file:
        if len(group) == 3:
            yield group
            group = []
        group.append(set(line))
    yield group
