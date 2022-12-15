from functools import cmp_to_key


def part1(file):
    index = 1
    index_sum = 0
    for left, right in parse_input(file):
        if check(left, right):
            index_sum += index
        index += 1
    return index_sum


def part2(file):
    packets = [eval(line) for line in file if line != '']
    divider1 = [[2]]
    divider2 = [[6]]
    packets.append(divider1)
    packets.append(divider2)
    packets.sort(key=cmp_to_key(lambda a, b: 1 if check(a, b) else -1), reverse=True)

    return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)


def parse_input(file):
    pair = []
    for line in file:
        if line == '':
            yield pair
            pair = []
            continue
        pair.append(eval(line))
    yield pair


def check(l, r):
    left, right = l, r
    left_int = isinstance(left, int)
    right_int = isinstance(right, int)

    if left_int and right_int:
        return None if right == left else right > left

    if left_int:
        left = [left]

    if right_int:
        right = [right]

    if len(left) > 0 and len(right) == 0:
        return False

    if len(left) == 0 and len(right) > 0:
        return True

    for i, left_val in enumerate(left):
        if len(right) > i:
            right_val = right[i]
            result = check(left_val, right_val)
            if result is None:
                continue
            return result

    return None if len(right) == len(left) else len(right) > len(left)
