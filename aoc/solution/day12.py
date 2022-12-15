from collections import deque
from aoc.exceptions import DesignError


def part1(file):
    heightmap = [list(map(lambda h: ord(h), line)) for line in file]
    width = len(heightmap[0])
    height = len(heightmap)

    start = find_marker(heightmap, ord('S'))
    end = find_marker(heightmap, ord('E'))

    heightmap[start[1]][start[0]] = ord('a')
    heightmap[end[1]][end[0]] = ord('z')

    visited = set()
    queue = deque()
    queue.append((start, 0))

    in_bounds = lambda p: 0 <= p[1] < height and 0 <= p[0] < width
    valid_step = lambda p, n: heightmap[n[1]][n[0]] - heightmap[p[1]][p[0]] < 2

    while len(queue):
        plot, length = queue.popleft()

        if plot == end:
            return length

        for neighbor in neighbors(plot):
            if not in_bounds(neighbor):
                continue
            if not valid_step(plot, neighbor):
                continue
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, length + 1))

    raise DesignError


def part2(file):
    heightmap = [list(map(lambda h: ord(h), line)) for line in file]
    width = len(heightmap[0])
    height = len(heightmap)

    start = find_marker(heightmap, ord('E'))
    heightmap[start[1]][start[0]] = ord('z')

    visited = set()
    queue = deque()
    queue.append((start, 0))

    in_bounds = lambda p: 0 <= p[1] < height and 0 <= p[0] < width
    valid_step = lambda p, n: heightmap[n[1]][n[0]] - heightmap[p[1]][p[0]] > -2

    while len(queue):
        plot, length = queue.popleft()

        if heightmap[plot[1]][plot[0]] == ord('a'):
            return length

        for neighbor in neighbors(plot):
            if not in_bounds(neighbor):
                continue
            if not valid_step(plot, neighbor):
                continue
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append((neighbor, length + 1))

    raise DesignError


def find_marker(heightmap, marker):
    for y, line in enumerate(heightmap):
        if marker in line:
            return line.index(marker), y
    raise DesignError


def neighbors(plot):
    yield plot[0] - 1, plot[1]
    yield plot[0] + 1, plot[1]
    yield plot[0], plot[1] - 1
    yield plot[0], plot[1] + 1
