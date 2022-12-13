def part1(file):
    assignment_pairs = [line_to_assignments(line) for line in file]
    return sum(1 if wholly_contained(pair) else 0 for pair in assignment_pairs)


def part2(file):
    assignment_pairs = [line_to_assignments(line) for line in file]
    return sum(1 if overlap(pair) else 0 for pair in assignment_pairs)


def line_to_assignments(line):
    return [assignment_to_set(assignment) for assignment in line.split(',')]


def assignment_to_set(assignment):
    f, t = (int(section) for section in assignment.split('-'))
    return set(range(f, t + 1))


def wholly_contained(pair):
    a, b = pair
    return a.issubset(b) or b.issubset(a)


def overlap(pair):
    a, b = pair
    return 1 if len(a.intersection(b)) else 0
