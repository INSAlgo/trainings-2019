from itertools import permutations


def is_magic(l):
    for k in range(3):
        # lines
        if l[3 * k] + l[3 * k + 1] + l[3 * k + 2] != 15:
            return False
        # columns
        if l[k] + l[3 + k] + l[6 + k] != 15:
            return False
    # diagonals
    if l[0] + l[4] + l[8] != 15:
        return False
    if l[2] + l[4] + l[6] != 15: 
        return False
    return True


def dist(start, comb):
    tot = 0
    for k in range(9):
        tot += abs(start[k] - comb[k])
    return tot


start_matrix = list()
for k in range(3):
    start_matrix += list(map(int, input().split()))
# try and generate all possible magic square, brut force
min_dist = 81
for square in permutations(list(range(1, 10)), 9):
    if is_magic(square):
        dist_with_start = dist(start_matrix, square)
        min_dist = min(min_dist, dist_with_start)

print(min_dist)
