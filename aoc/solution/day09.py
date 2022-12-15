def part1(file):
    return part2(file, 2)


def part2(file, length=10):
    rope = [{'x': 0, 'y': 0} for _ in range(0, length)]
    head = length - 1

    visited = set()
    for line in file:
        direction, distance = instruction(line)
        for _ in range(0, distance):
            move(rope[head], direction)
            for i in range(head, 0, -1):
                if not update_tail(rope[i], rope[i-1]):
                    break
            visited.add(f"{rope[0]['x']},{rope[0]['y']}")

    return len(visited)


def instruction(line):
    direction, distance = line.split(' ')
    return direction, int(distance)


def move(point, direction):
    if direction == 'U':
        point['y'] += 1
    if direction == 'D':
        point['y'] -= 1
    if direction == 'R':
        point['x'] += 1
    if direction == 'L':
        point['x'] -= 1


def update_tail(head, tail):
    if not adjacent(head, tail):
        x_dist = tail['x'] - head['x']
        y_dist = tail['y'] - head['y']

        if x_dist != 0:
            move(tail, 'L' if x_dist > 0 else 'R')
        if y_dist != 0:
            move(tail, 'D' if y_dist > 0 else 'U')

        return True
    return False


def adjacent(head, tail):
    if abs(head['x'] - tail['x']) > 1:
        return False
    if abs(head['y'] - tail['y']) > 1:
        return False
    return True
