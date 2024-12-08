import pandas as pd

from utils import read_matrix

file_path = "./data/day04.txt"
matrix = read_matrix(file_path)


def check_char(m, i, j, char):
    if 0 <= i < m.shape[0] and 0 <= j < m.shape[1]:
        return m[i, j] == char
    return False


def search_diagonal(matrix, i, j, char):
    diagonal_positions = [
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    ]
    positions = []
    for x, y in diagonal_positions:
        if check_char(matrix, x, y, char):
            positions.append((x, y))
    return positions


def search_mas(m, i, j):
    A_pos = []
    if m[i, j] == "M":
        pos = search_diagonal(m, i, j, "A")
        # Una M puede ser el inicio de varios MAS
        for i1, j1 in pos:
            # Una vez encontrada la A, sabemos las posicion de la S
            di, dj = i1 - i, j1 - j
            if check_char(m, i1 + di, j1 + dj, "S"):
                A_pos.append((i1, j1))

    return A_pos


# Buscamos MAS en diagonal y guardamos las posiciones
# de la A. Si dos MAS comparten la misma A, entonces
# están en forma de cruz
all_pos = []
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        all_pos.extend(search_mas(matrix, i, j))


print(pd.DataFrame(all_pos).duplicated().sum())
