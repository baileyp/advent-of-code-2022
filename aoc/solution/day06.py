from aoc.exceptions import DesignError


def part1(file, marker_length=4):
    signal = file.single_line()
    for cursor in range(marker_length-1, len(signal)):
        packet = signal[cursor - marker_length:cursor]
        if len(set(packet)) == marker_length:
            return cursor
    raise DesignError


def part2(file):
    return part1(file, 14)
