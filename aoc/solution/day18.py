from collections import deque


def part1(file):
    surface_area = 0
    cubes = set()
    for line in file:
        new_cube = tuple(int(n) for n in line.split(','))
        sides = 6
        for cube in cubes:
            if adjacent(cube, new_cube):
                sides -= 2
        surface_area += sides
        cubes.add(new_cube)
    return surface_area


def part2(file):
    surface_area = 0
    cubes = set()
    for line in file:
        new_cube = tuple(int(n) for n in line.split(','))
        sides = 6
        for cube in cubes:
            if adjacent(cube, new_cube):
                sides -= 2
        surface_area += sides
        cubes.add(new_cube)

    return surface_area - sum(get_surface_area(v) for v in find_voids(cubes))


def adjacent(cube_a, cube_b):
    a_x, a_y, a_z = cube_a
    b_x, b_y, b_z = cube_b

    if a_x == b_x and a_y == b_y:
        return abs(a_z - b_z) == 1

    if a_x == b_x and a_z == b_z:
        return abs(a_y - b_y) == 1

    if a_y == b_y and a_z == b_z:
        return abs(a_x - b_x) == 1

    return False


def find_voids(cubes):
    min_x = min(x for x, y, z in cubes)
    max_x = max(x for x, y, z in cubes)
    min_y = min(y for x, y, z in cubes)
    max_y = max(y for x, y, z in cubes)
    min_z = min(z for x, y, z in cubes)
    max_z = max(z for x, y, z in cubes)

    bounds = ((min_x, min_y, min_z), (max_x, max_y, max_z))
    voids = []

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                point = (x, y, z)
                if point in cubes or any(map(lambda v: point in v, voids)):
                    continue
                void = void_at_point(point, cubes, bounds)
                if void is None:
                    continue
                voids.append(void)

    return voids


def void_at_point(point, cubes, bounds):
    if point in cubes:
        return None

    void = set([point])
    queue = deque([point])

    while len(queue):
        p = queue.popleft()

        for n in neighbors(p):
            if n in cubes or n in void:
                continue
            if out_of_bounds(n, bounds):
                return None
            void.add(n)
            queue.append(n)

    return void


def neighbors(cube):
    x, y, z = cube
    yield x, y, z + 1
    yield x, y, z - 1
    yield x, y + 1, z
    yield x, y - 1, z
    yield x + 1, y, z
    yield x - 1, y, z


def out_of_bounds(point, bounds):
    x, y, z = point
    return any([
        x < bounds[0][0],
        x > bounds[1][0],
        y < bounds[0][1],
        y > bounds[1][1],
        z < bounds[0][2],
        z > bounds[1][2],
    ])


def get_surface_area(cubes):
    surface_area = 6 * len(cubes)
    for check_cube in cubes:
        for cube in cubes:
            if adjacent(cube, check_cube):
                surface_area -= 1

    return surface_area
