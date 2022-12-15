from collections import deque
from functools import reduce
from math import floor


def part1(file):
    monkeys = list(get_monkeys(file))

    for _ in range(0, 20):
        for monkey in monkeys:
            while len(monkey['items']):
                item = monkey['items'].popleft()
                monkey['inspected'] += 1
                worry = (lambda old: eval(monkey['operation']))(item)
                worry = floor(worry / 3)

                throw_to = monkeys[monkey['true' if worry % monkey['divisible'] == 0 else 'false']]
                throw_to['items'].append(worry)

    thrown = sorted(list(map(lambda m: m['inspected'], monkeys)), reverse=True)
    return thrown[0] * thrown[1]


def part2(file):
    monkeys = list(get_monkeys(file))

    worry_divisor = reduce(lambda a, b: a * b, map(lambda m: m['divisible'], monkeys))

    for _ in range(0, 10000):
        for monkey in monkeys:
            while len(monkey['items']):
                item = monkey['items'].popleft() % worry_divisor
                monkey['inspected'] += 1
                worry = (lambda old: eval(monkey['operation']))(item)

                throw_to = monkeys[monkey['true' if worry % monkey['divisible'] == 0 else 'false']]
                throw_to['items'].append(worry)

    thrown = sorted(list(map(lambda m: m['inspected'], monkeys)), reverse=True)
    return thrown[0] * thrown[1]


def get_monkeys(file):
    monkey = {'inspected': 0}
    for line in file:
        if line == '':
            yield monkey
            monkey = {'inspected': 0}
        if 'Monkey' in line:
            monkey['id'] = int(line[7:8])
        elif 'Starting items' in line:
            monkey['items'] = deque(int(worry) for worry in line[16:].split(', '))
        elif 'Operation' in line:
            monkey['operation'] = line[17:]
        elif 'Test' in line:
            monkey['divisible'] = int(line[19:])
        elif 'true' in line:
            monkey['true'] = int(line[25:])
        elif 'false' in line:
            monkey['false'] = int(line[26:])
    yield monkey
