import re
from collections import deque
from functools import reduce
from aoc.util import defaultlist


def part1(file):
    stacks, moves = parse_input(file)

    for qty, frm, to in moves:
        for _ in range(0, qty):
            stacks[to - 1].append(stacks[frm - 1].pop())

    return reduce(lambda a, b: a + b, (stack.pop() for stack in stacks))


def part2(file):
    stacks, moves = parse_input(file)

    for qty, frm, to in moves:
        group = deque()
        for _ in range(0, qty):
            group.appendleft(stacks[frm - 1].pop())
        stacks[to - 1].extend(group)

    return reduce(lambda a, b: a + b, (stack.pop() for stack in stacks))


def parse_input(file):
    stacks = defaultlist(lambda: deque())
    moves = []
    for line in file.raw():
        if line == '' or re.match("^[1-9 ]+$", line):
            continue
        elif re.match("move", line):
            moves.append([int(m) for m in re.findall("[0-9]+", line.strip())])
        else:
            crates = [line[i:i + 4] for i in range(0, len(line), 4)]
            for i, crate in enumerate(crates):
                match = re.search("[A-Z]", crate)
                if match:
                    stacks[i].appendleft(match.group())
    return stacks, moves
