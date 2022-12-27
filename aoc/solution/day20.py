from collections import deque


def part1(file):
    nums = [int(line) for line in file]
    list_size = len(nums)

    order = [i for i in range(0, list_size)]

    for i in range(0, list_size):
        position = order.index(i)
        shift = nums[position]
        if shift == 0:
            continue

        nums = move(nums, position, shift)
        order = move(order, position, shift)

    index_of_zero = nums.index(0)
    positions = []
    foo = deque(nums)
    foo.rotate(-index_of_zero)
    foo.rotate(-1000)
    positions.append(foo[0])
    foo.rotate(-1000)
    positions.append(foo[0])
    foo.rotate(-1000)
    positions.append(foo[0])

    return sum(positions)


def part2(file):
    nums = [int(line) * 811589153 for line in file]
    list_size = len(nums)

    order = [i for i in range(0, list_size)]

    for _ in range(0, 10):
        for i in range(0, list_size):
            position = order.index(i)
            shift = nums[position]
            if shift == 0:
                continue

            nums = move(nums, position, shift)
            order = move(order, position, shift)

    index_of_zero = nums.index(0)
    positions = []
    foo = deque(nums)
    foo.rotate(-index_of_zero)
    foo.rotate(-1000)
    positions.append(foo[0])
    foo.rotate(-1000)
    positions.append(foo[0])
    foo.rotate(-1000)
    positions.append(foo[0])

    return sum(positions)


def move(sequence, position, shift):
    length = len(sequence)
    if abs(shift) >= length:
        if shift < 0:
            shift = -(abs(shift) % (length - 1))
        else:
            shift %= length - 1

    new_position = position + shift
    if shift < 0:
        if new_position <= 0:
            new_position = length - 1 + new_position
    else:
        if new_position >= length - 1:
            new_position = new_position - length + 1

    new_sequence = list()

    if position > new_position:
        left = sequence[0:new_position]
        middle = deque(sequence[new_position:position + 1])
        right = sequence[position + 1:]

        middle.appendleft(middle.pop())
        new_sequence.extend(left)
        new_sequence.extend(middle)
        new_sequence.extend(right)
    else:
        left = sequence[0:position]
        middle = deque(sequence[position:new_position + 1])
        right = sequence[new_position + 1:]

        middle.append(middle.popleft())

        new_sequence.extend(left)
        new_sequence.extend(middle)
        new_sequence.extend(right)

    return new_sequence
