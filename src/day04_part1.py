from utils import read_matrix

file_path = "./data/day04.txt"
matrix = read_matrix(file_path)


def check_char(m, i, j, char):
    if 0 <= i < m.shape[0] and 0 <= j < m.shape[1]:
        return m[i, j] == char
    return False


def search_adjacent(matrix, i, j, char):
    adjacent_positions = [
        (i - 1, j),
        (i + 1, j),
        (i, j - 1),
        (i, j + 1),
        (i - 1, j - 1),
        (i - 1, j + 1),
        (i + 1, j - 1),
        (i + 1, j + 1),
    ]
    positions = []
    for x, y in adjacent_positions:
        if check_char(matrix, x, y, char):
            positions.append((x, y))
    return positions


def search_xmas(m, i, j):
    total = 0
    if m[i, j] == "X":
        pos = search_adjacent(m, i, j, "M")
        # Una X puede ser el inicio de varios XMAS
        # iteramos por todas las M adyacentes
        for i1, j1 in pos:
            # Una vez encontrada la M, sabemos las posiciones exactas
            # de la A y la S
            di, dj = i1 - i, j1 - j
            if check_char(m, i1 + di, j1 + dj, "A") and check_char(
                m, i1 + 2 * di, j1 + 2 * dj, "S"
            ):
                total += 1
    return total


# Iterate over the 2D numpy array with positions
total = 0
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        total += search_xmas(matrix, i, j)


print(total)
