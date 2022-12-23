from collections import deque


def part1(file, num_rocks=2022):
    jet_pattern = deque(file.single_line())
    shapes = deque([
        # h-bar
        {(0, 0), (1, 0), (2, 0), (3, 0)},
        # cross
        {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)},
        # angle
        {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
        # v-bar
        {(0, 0), (0, 1), (0, 2), (0, 3)},
        # block
        {(0, 0), (1, 0), (0, 1), (1, 1)},
    ])
    cave = set([(x, -1) for x in range(0, 7)])
    height = -1

    for _ in range(0, num_rocks):
        shape = init_shape(shapes[0], height)

        while True:
            # Jet blast
            moved = move_shape(shape, jet_pattern[0])
            jet_pattern.rotate(-1)
            if len(moved & cave) > 0:
                # Jet blast collided, reset
                moved = shape
            # Fall
            shape = moved
            moved = move_shape(shape)
            if len(moved & cave) == 0:
                # shape drops
                shape = moved
            else:
                # shape at rest
                break

        cave |= shape
        height = max(height, *(y for _, y in cave))
        shapes.rotate(-1)

    return height + 1


def part2(file):
    # lol
    return part1(file, 1000000000000)


def init_shape(shape, lowest):
    return set(map(mover(2, lowest + 4), shape))


def move_shape(shape, direction='v'):
    if direction == 'v':
        return set(map(mover(0, -1), shape))

    if direction == '>' and max(x for x, _ in shape) < 6:
        return set(map(mover(1, 0), shape))

    if direction == '<' and min(x for x, _ in shape) > 0:
        return set(map(mover(-1, 0), shape))

    return shape


def mover(x_offset, y_offset):
    def inner(shape):
        x, y = shape
        return tuple([x + x_offset, y + y_offset])

    return inner
