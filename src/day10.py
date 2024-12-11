import numpy as np

from utils import read_matrix


def dfs_part1(m, r, c, found):
    if m[r, c] == 9 and (r, c) not in found:
        found.append((r, c))
        return 1

    adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    return sum(
        dfs_part1(m, r1, c1, found)
        for r1, c1 in adj
        if 0 <= r1 < m.shape[0]
        and 0 <= c1 < m.shape[1]
        and ((m[r1, c1] - m[r, c]) == 1)
    )


def dfs_part2(m, r, c, rating, origen):
    if m[r, c] == 0:
        rating[origen] = 0

    if m[r, c] == 9:
        rating[origen] += 1
        return 1

    adj = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

    return sum(
        dfs_part2(m, r1, c1, rating, origen)
        for r1, c1 in adj
        if 0 <= r1 < m.shape[0]
        and 0 <= c1 < m.shape[1]
        and ((m[r1, c1] - m[r, c]) == 1)
    )


m = read_matrix("data/day10_test.txt").astype(int)
print(m)

a, _ = np.where(m == 9)
print(len(a))

# scores = [dfs(m, r, c, []) for r, c in zip(*np.where(m == 0))]
# print(sum(scores))

rating = {}
for r, c in zip(*np.where(m == 0)):
    print(dfs_part2(m, r, c, rating, (int(r), int(c))))

print(sum(rating.values()))
