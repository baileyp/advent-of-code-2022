from functools import reduce


def part1(file):
    grid = list(map(lambda line: [int(cell) for cell in line], file))

    visible = set()
    for row_index, row in enumerate(grid):
        find_visible_row(row, row_index, visible)

    for col_index in range(0, len(grid[0])):
        find_visible_col(grid, col_index, visible)

    return len(visible)


def part2(file):
    grid = list(map(lambda line: [int(cell) for cell in line], file))
    width = len(grid[0])
    height = len(grid)

    max_score = 0
    for row_index in range(1, height - 1):
        for col_index in range(1, width - 1):
            max_score = max(max_score, score_plot(grid, width, height, col_index, row_index))

    return max_score


def find_visible_row(row, row_index, visible):
    tallest = -1
    for col_index, tree in enumerate(row):
        if tree > tallest:
            visible.add(f"{col_index},{row_index}")
        tallest = max(tallest, tree)

    tallest = -1
    for col_index in range(len(row) - 1, 0, -1):
        tree = row[col_index]
        if tree > tallest:
            visible.add(f"{col_index},{row_index}")
        tallest = max(tallest, tree)


def find_visible_col(grid, col_index, visible):
    tallest = -1
    height = len(grid)
    for row_index in range(0, height):
        tree = grid[row_index][col_index]
        if tree > tallest:
            visible.add(f"{col_index},{row_index}")
        tallest = max(tallest, tree)

    tallest = -1
    for row_index in range(height - 1, 0, -1):
        tree = grid[row_index][col_index]
        if tree > tallest:
            visible.add(f"{col_index},{row_index}")
        tallest = max(tallest, tree)

def score_plot(grid, width, height, col_index, row_index):
    considered = grid[row_index][col_index]
    visible = {'up': 0, 'down': 0, 'right': 0, 'left': 0}

    # up
    for i in range(max(0, row_index - 1), -1, -1):
        tree = grid[i][col_index]
        visible['up'] += 1
        if tree >= considered:
            break

    # down
    for i in range(min(height - 1, row_index + 1), height):
        tree = grid[i][col_index]
        visible['down'] += 1
        if tree >= considered:
            break

    # right
    for i in range(min(width - 1, col_index + 1), width):
        tree = grid[row_index][i]
        visible['right'] += 1
        if tree >= considered:
            break

    # left
    for i in range(max(0, col_index - 1), -1, -1):
        tree = grid[row_index][i]
        visible['left'] += 1
        if tree >= considered:
            break

    return reduce(lambda a, b: a * b, visible.values())
