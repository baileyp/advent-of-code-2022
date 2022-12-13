score_per_move = {'A': 1, 'B': 2, 'C': 3}


def part1(file):
    return sum(score_round(*line.split(' ')) for line in file)


def part2(file):
    return sum(score_round2(*line.split(' ')) for line in file)


def score_round(opponent, player):
    if player == 'X':
        return 1 + {'A': 3, 'B': 0, 'C': 6}[opponent]
    if player == 'Y':
        return 2 + {'A': 6, 'B': 3, 'C': 0}[opponent]
    return 3 + {'A': 0, 'B': 6, 'C': 3}[opponent]


def score_round2(opponent, player):
    if player == 'Y':
        return 3 + score_per_move[opponent]
    if player == 'X':
        return score_per_move[{'A': 'C', 'B': 'A', 'C': 'B'}[opponent]]
    return 6 + score_per_move[{'A': 'B', 'B': 'C', 'C': 'A'}[opponent]]
