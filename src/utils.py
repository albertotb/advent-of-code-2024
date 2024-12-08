import numpy as np


def read_matrix(file_path):
    with open(file_path, "r") as file:
        data = file.readlines()
    return np.array([list(line.strip()) for line in data])


def print_matrix(m):
    for r in m:
        print("".join(r))
