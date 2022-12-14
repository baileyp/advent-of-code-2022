from aoc.exceptions import DesignError


def part1(file):
    filesystem = tree(iter(file))

    return sum(b for b in walk(filesystem, get_size) if b <= 100000)


def part2(file):
    filesystem = tree(iter(file))
    dirs = [b for b in walk(filesystem, get_size)]

    capacity = 70000000
    needed = 30000000
    used = max(dirs)

    available = capacity - used
    must_delete = needed - available

    return min(b for b in dirs if b >= must_delete)


def walk(pwd, fn):
    for entry in pwd.values():
        if isinstance(entry, dict):
            yield from walk(entry, fn)
            yield fn(entry)


def get_size(pwd):
    size = 0
    for entry in pwd.values():
        if isinstance(entry, int):
            size += entry
        else:
            size += get_size(entry)
    return size


def tree(input):
    directory = dict()

    try:
        while True:
            line = next(input)
            if line[2:4] == 'ls':
                line = next(input)
                while line[0] != '$':
                    if line[0:3] == 'dir':
                        directory[line[4:]] = dict()
                    else:
                        bytes, filename = line.split(' ')
                        directory[filename] = int(bytes)
                    line = next(input)
            if line[2:4] == 'cd':
                dir = line[5:]
                if dir == '..':
                    return directory
                directory[dir] = tree(input)
    except:
        return directory

    raise DesignError
