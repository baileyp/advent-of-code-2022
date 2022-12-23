import re
from collections import deque

from aoc.util import memoize


def part1(file):
    valve_map = dict()
    valves = dict()
    for line in file:
        valve, flow_rate, tunnels = parse_line(line)
        valves[valve] = flow_rate
        valve_map[valve] = tunnels

    valves_to_open = [v for v, r in valves.items() if r > 0]
    first_valve = 'AA'
    time_limit = 30
    maximum_pressure = 0

    stack = [[[first_valve], 0, {}]]

    while len(stack):
        path, minutes_elapsed, open_valves = stack.pop()
        current_valve = path[-1]

        if minutes_elapsed >= time_limit or len(path) == len(valves_to_open) + 1:
            pressure_released = 0

            for valve, minute_opened in open_valves.items():
                minutes_opened = max(time_limit - minute_opened, 0)
                pressure_released += valves[valve] * minutes_opened

            maximum_pressure = max(maximum_pressure, pressure_released)
        else:
            for next_valve in valves_to_open:
                if next_valve not in open_valves.keys():
                    travel_time = shorest_path_length(valve_map, current_valve, next_valve)

                    new_open_valves = open_valves.copy()
                    new_open_valves[next_valve] = minutes_elapsed + travel_time + 1

                    stack.append([path + [next_valve], new_open_valves[next_valve], new_open_valves])

    return maximum_pressure


def part2(file):
    return None


def parse_line(line):
    matches = re.findall('^Valve ([A-Z]+) has flow rate=(\d+).+valves? (.+)$', line).pop()
    return matches[0], int(matches[1]), matches[2].split(', ')


def shorest_path_length(valve_map, from_valve, to_valve):
    @memoize
    def inner(start, end):
        queue = deque([[start]])
        visited = set()

        if start == end:
            return len([start]) - 1

        while len(queue) > 0:
            path = queue.popleft()
            node = path[-1]

            if node not in visited:
                for neighbor in valve_map[node]:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)

                    if neighbor == end:
                        return len(new_path) - 1

                visited.add(node)

        return None
    return inner(from_valve, to_valve)