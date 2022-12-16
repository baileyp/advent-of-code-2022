def part1(file):
    print_cave = False
    cave = set()
    lines = list(iter(file))
    unique_paths = set(lines)
    for line in unique_paths:
        path = [Plot(*coord.split(',')) for coord in line.split(' -> ')]
        draw_path(cave, path)

    lowest = max(p[1] for p in cave)
    sands = set()
    path = set()
    start = 500

    sand = Plot(start, 0)
    while sand.y < lowest:
        path.add(sand.coord())
        # down
        sand.y += 1
        if sand.coord() not in cave:
            continue

        # down and left
        sand.x -= 1
        if sand.coord() not in cave:
            continue

        # down and right
        sand.x += 2
        if sand.coord() not in cave:
            continue

        # at rest
        sand.x -= 1
        sand.y -= 1
        cave.add(sand.coord())
        sands.add(sand.coord())
        sand = Plot(start, 0)

    path.add(sand.coord())

    if print_cave:
        print('')
        for _ in range(0, 3):
            print('    ', end='')
            for x in range(min(p[0] for p in cave) - 2, max(p[0] for p in cave) + 2):
                print(str(x)[_], end='')
            print('')

        print('')
        for y in range(min(p[1] for p in cave) - 2, max(p[1] for p in cave) + 2):
            print(('    ' + str(y))[-4:], end='')
            for x in range(min(p[0] for p in cave) - 2, max(p[0] for p in cave) + 2):
                if (x, y) in sands:
                    print('\033[38;5;178mo\033[0m', end='')
                elif (x, y) in cave:
                    print('\033[38;5;240m#\033[0m', end='')
                else:
                    print('\033[38;5;33m~\033[0m' if (x, y) in path else ' ', end='')
            print('')

    return len(sands)


def part2(file):
    print_cave = False
    cave = set()
    lines = list(iter(file))
    unique_paths = set(lines)
    for line in unique_paths:
        path = [Plot(*coord.split(',')) for coord in line.split(' -> ')]
        draw_path(cave, path)

    lowest = max(p[1] for p in cave)
    floor = lowest + 2
    sands = set()
    path = set()
    start = 500

    sand = Plot(start, 0)
    while sand.coord() not in cave:
        path.add(sand.coord())
        # down
        sand.y += 1
        if sand.coord() not in cave and sand.y < floor:
            continue

        # down and left
        sand.x -= 1
        if sand.coord() not in cave and sand.y < floor:
            continue

        # down and right
        sand.x += 2
        if sand.coord() not in cave and sand.y < floor:
            continue

        # at rest
        sand.x -= 1
        sand.y -= 1
        cave.add(sand.coord())
        sands.add(sand.coord())
        sand = Plot(start, 0)

    path.add(sand.coord())

    if print_cave:
        print('')
        for _ in range(0, 3):
            print('    ', end='')
            for x in range(min(p[0] for p in cave) - 2, max(p[0] for p in cave) + 2):
                print(str(x)[_], end='')
            print('')

        print('')
        for y in range(min(p[1] for p in cave) - 2, max(p[1] for p in cave) + 2):
            print(('    ' + str(y))[-4:], end='')
            for x in range(min(p[0] for p in cave) - 2, max(p[0] for p in cave) + 2):
                if (x, y) in sands:
                    print('\033[38;5;178mo\033[0m', end='')
                elif (x, y) in cave:
                    print('\033[38;5;240m#\033[0m', end='')
                else:
                    print('\033[38;5;33m~\033[0m' if (x, y) in path else ' ', end='')
            print('')

    return len(sands)


def draw_path(cave, path):
    for i in range(0, len(path) - 1):
        a, b = path[i], path[i + 1]

        for p in steps(a, b):
            cave.add((p.x, p.y))


def steps(a, b):
    if a.x == b.x:
        if a.y < b.y:
            for y in range(a.y, b.y + 1):
                yield Plot(a.x, y)
        else:
            for y in range(b.y, a.y + 1):
                yield Plot(a.x, y)
    else:
        if a.x < b.x:
            for x in range(a.x, b.x + 1):
                yield Plot(x, a.y)
        else:
            for x in range(b.x, a.x + 1):
                yield Plot(x, a.y)


class Plot:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def coord(self):
        return tuple((self.x, self.y))
