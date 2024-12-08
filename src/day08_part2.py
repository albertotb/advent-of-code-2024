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
            # derivada
            dr, dc = r2 - r1, c2 - c1

            # Avanzamos en la direccion (dr, dc) y -(dr, dc)
            # desde (r1, c1) o (r2, c2) (da igual cual) tantos
            # pasos como el tam max de la matrix (se puede hacer
            # mas eficiente parando en el borde)
            for step in range(max(*m.shape)):
                pr1, pc1 = r2 + step * dr, c2 + step * dc

                if pr1 >= 0 and pr1 < m.shape[0] and pc1 >= 0 and pc1 < m.shape[1]:
                    n[pr1, pc1] = "#"

                pr2, pc2 = r2 - step * dr, c2 - step * dc

                if pr2 >= 0 and pr2 < m.shape[0] and pc2 >= 0 and pc2 < m.shape[1]:
                    n[pr2, pc2] = "#"

a, b = np.where(n != ".")
print(len(a))
print_matrix(n)
