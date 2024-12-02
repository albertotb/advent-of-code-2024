import numpy as np


def is_safe(line):
    d = np.diff(line)
    d_abs = np.abs(d)
    safe = (
        ((d < 0).all() or (d > 0).all()) and (d_abs.max() <= 3) and (d_abs.min() >= 1)
    )

    return safe


# Read the file
with open("./data/day02.txt", "r") as file:
    data = [list(map(int, line.split())) for line in file.readlines()]

res = []
for line in data:
    if is_safe(line):
        res.append(True)
    else:
        for missing in range(len(line)):
            if is_safe(np.delete(line, missing)):
                res.append(True)
                break
        else:
            res.append(False)

print(sum(res))


# Pandas sol

# # Find the maximum length of the rows
# max_length = max(len(row) for row in data)

# # Pad the rows with np.nan
# a = np.array([row + [np.nan] * (max_length - len(row)) for row in data])

# # a = np.loadtxt("data/day02_test.txt", dtype=int, delimiter=" ")
# # a = np.loadtxt("data/day02.txt", dtype=int, delimiter=" ")

# a = pd.DataFrame(a)

# d = a.diff(axis=1).ffill(axis=1).loc[:, 1:]

# all_dec = (d < 0).all(axis=1)
# all_inc = (d > 0).all(axis=1)
# max_diff = d.abs().max(axis=1)
# min_diff = d.abs().min(axis=1)

# safe = (all_dec | all_inc) & (max_diff <= 3) & (min_diff >= 1)

# print(safe.sum())
