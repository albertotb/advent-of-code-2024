from itertools import combinations

import numpy as np

from utils import print_matrix, read_matrix

m = read_matrix("data/day08.txt")
print(m.shape)
n = m.copy()

unique_elements = np.unique(m)

for freq in unique_elements:
    if freq != ".":
        r, c = np.where(m == freq)

        for (r1, c1), (r2, c2) in combinations(zip(r, c), 2):
            # punto medio entre 2 puntos
            pr1, pc1 = 2 * r1 - r2, 2 * c1 - c2
            pr2, pc2 = 2 * r2 - r1, 2 * c2 - c1

            if pr1 >= 0 and pr1 < m.shape[0] and pc1 >= 0 and pc1 < m.shape[1]:
                n[pr1, pc1] = "#"

            if pr2 >= 0 and pr2 < m.shape[0] and pc2 >= 0 and pc2 < m.shape[1]:
                n[pr2, pc2] = "#"

a, b = np.where(n == "#")
print(len(a))
print_matrix(n)
