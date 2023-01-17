import re


def part1(file):
    monkeys = {}
    for line in file:
        monkeys[line[0:4]] = eval('lambda m: ' + re.sub("([a-z]{4})", r"m['\1'](m)", line[6:]))

    return int(monkeys['root'](monkeys))
