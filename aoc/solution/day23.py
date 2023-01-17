from collections import defaultdict, deque

strategies = {
    'N': {
        'condition': lambda elves, elf: all(n not in elves for n in north_neighbors(elf)),
        'move': lambda proposed, col, row, elf: proposed[(col, row - 1)].append(elf),
    },
    'S': {
        'condition': lambda elves, elf: all(n not in elves for n in south_neighbors(elf)),
        'move': lambda proposed, col, row, elf: proposed[(col, row + 1)].append(elf),
    },
    'W': {
        'condition': lambda elves, elf: all(n not in elves for n in west_neighbors(elf)),
        'move': lambda proposed, col, row, elf: proposed[(col - 1, row)].append(elf),
    },
    'E': {
        'condition': lambda elves, elf: all(n not in elves for n in east_neighbors(elf)),
        'move': lambda proposed, col, row, elf: proposed[(col + 1, row)].append(elf),
    },
}


def part1(file):
    elves = parse_input(file)
    # print_elves(elves)
    turns = deque(['N', 'S', 'W', 'E'])
    for _ in range(0, 10):
        proposed = defaultdict(lambda: [])
        for elf in elves:
            col, row = elf
            if all(n not in elves for n in neighbors(elf)):
                proposed[(col, row)].append(elf)
            else:
                for turn in turns:
                    strategy = strategies[turn]
                    if strategy['condition'](elves, elf):
                        strategy['move'](proposed, col, row, elf)
                        break
                else:
                    proposed[(col, row)].append(elf)

        elves = set()
        for target, proposing_elves in proposed.items():
            if len(proposing_elves) > 1:
                for elf in proposing_elves:
                    elves.add(elf)
            else:
                elves.add(target)

        turns.rotate(-1)
        # print_elves(elves)

    empties = 0
    for col in range(min(c for c, _ in elves), max(c for c, _ in elves) + 1):
        for row in range(min(r for _, r in elves), max(r for _, r in elves) + 1):
            if (col, row) not in elves:
                empties += 1

    return empties


def part2(file):
    elves = parse_input(file)
    turns = deque(['N', 'S', 'W', 'E'])
    round = 0
    while True:
        round += 1
        proposed = defaultdict(lambda: [])
        for elf in elves:
            col, row = elf
            if all(n not in elves for n in neighbors(elf)):
                proposed[(col, row)].append(elf)
            else:
                for turn in turns:
                    strategy = strategies[turn]
                    if strategy['condition'](elves, elf):
                        strategy['move'](proposed, col, row, elf)
                        break
                else:
                    proposed[(col, row)].append(elf)

        elves = set()
        for target, proposing_elves in proposed.items():
            if len(proposing_elves) > 1:
                for elf in proposing_elves:
                    elves.add(elf)
            else:
                elves.add(target)

        turns.rotate(-1)

        if all(len(proposing_elves) == 1 and proposing_elves[0] == target for target, proposing_elves in proposed.items()):
            break

    return round



def parse_input(file):
    grid = set()
    for row, line in enumerate(file):
        for col, cell in enumerate(line):
            if cell == '#':
                grid.add((col, row))

    return grid


def neighbors(position):
    col, row = position
    yield col - 1, row - 1
    yield col - 1, row
    yield col - 1, row + 1
    yield col + 1, row - 1
    yield col + 1, row
    yield col + 1, row + 1
    yield col, row - 1
    yield col, row + 1


def north_neighbors(position):
    col, row = position
    yield col - 1, row - 1
    yield col, row - 1
    yield col + 1, row - 1


def south_neighbors(position):
    col, row = position
    yield col - 1, row + 1
    yield col, row + 1
    yield col + 1, row + 1


def west_neighbors(position):
    col, row = position
    yield col - 1, row - 1
    yield col - 1, row
    yield col - 1, row + 1


def east_neighbors(position):
    col, row = position
    yield col + 1, row - 1
    yield col + 1, row
    yield col + 1, row + 1


def print_elves(elves):
    print('')
    for row in range(min(r for _, r in elves), max(r for _, r in elves) + 1):
        for col in range(min(c for c, _ in elves), max(c for c, _ in elves) + 1):
            print("#" if (col, row) in elves else ".", end="")
        print("")
