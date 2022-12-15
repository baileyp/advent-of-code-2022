def part1(file):
    cycle = 1
    x = 1
    strengths = []

    for instruction in file:
        is_noop = instruction == 'noop'
        cycles = 1 if is_noop else 2
        for _ in range(0, cycles):
            if cycle in (20, 60, 100, 140, 180, 220):
                strengths.append(cycle * x)
            cycle += 1
        if not is_noop:
            x += int(instruction[5:])

    return sum(strengths)


def part2(file):
    cycle = 0
    sprite = [0, 1, 2]
    line = ''
    crt = []

    for instruction in file:
        is_noop = instruction == 'noop'
        cycles = 1 if is_noop else 2

        for _ in range(0, cycles):
            if cycle % 40 == 0:
                crt.append(line)
                line = ''
            line += '█' if cycle % 40 in sprite else ' '
            cycle += 1
        if not is_noop:
            center = sprite[1] + int(instruction[5:])
            sprite = [center - 1, center, center + 1]

    crt.append(line)
    return "\n".join(crt)
