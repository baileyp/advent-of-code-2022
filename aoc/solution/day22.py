from collections import deque


def part1(file):
    grid, path = parse_input(file)
    position = find_start(grid)
    facings = ['R', 'D', 'L', 'U']
    facing = deque(facings)

    for instruction in path:
        if instruction in {'L', 'R'}:
            facing.rotate(1 if instruction == 'L' else -1)
            continue

        for _ in range(0, instruction):
            step = next_position(position, grid, facing[0])
            if grid[step] == '#':
                break
            position = step

    col, row = position
    return 1000 * (row + 1) + 4 * (col + 1) + facings.index(facing[0])


def part2(file):
    grid, path = parse_input(file)
    position = find_start(grid)
    facings = ['R', 'D', 'L', 'U']
    facing = deque(facings)

    for instruction in path:
        if instruction in {'L', 'R'}:
            facing.rotate(1 if instruction == 'L' else -1)
            continue

        for _ in range(0, instruction):
            step = next_position_cube(position, grid, facing[0])
            if grid[step] == '#':
                break
            position = step

    col, row = position
    return 1000 * (row + 1) + 4 * (col + 1) + facings.index(facing[0])


def parse_input(file):
    grid = []
    path = ''
    map_scanned = False
    for line in file.raw():
        if '\n' == line:
            map_scanned = True
            continue
        if map_scanned:
            path = parse_path(line)
        else:
            grid.append(line)

    return optimize_grid(grid), path


def parse_path(raw_path):
    instructions = []
    current = ""
    for char in raw_path:
        if char in {'L', 'R'}:
            instructions.append(int(current))
            instructions.append(char)
            current = ""
        else:
            current += char

    instructions.append(int(current))

    return instructions


def optimize_grid(grid):
    optimized = dict()

    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell in {'.', '#'}:
                optimized[(col, row)] = cell

    return optimized


def find_start(grid):
    return min(col for col, row in grid.keys() if row == 0), 0


def next_position(position, grid, direction):
    col, row = position
    if direction == 'U':
        row -= 1
        if (col, row) in grid:
            return col, row
        return col, max(r for c, r in grid.keys() if c == col)

    if direction == 'D':
        row += 1
        if (col, row) in grid:
            return col, row
        return col, min(r for c, r in grid.keys() if c == col)

    if direction == 'R':
        col += 1
        if (col, row) in grid:
            return col, row
        return min(c for c, r in grid.keys() if r == row), row

    if direction == 'L':
        col -= 1
        if (col, row) in grid:
            return col, row
        return max(c for c, r in grid.keys() if r == row), row


def match_edges(grid, size=4):
    return None


def next_position_cube(position, grid, direction):
    return next_position(position, grid, direction)
