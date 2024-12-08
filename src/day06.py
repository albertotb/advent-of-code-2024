import numpy as np
import pandas as pd

from utils import read_matrix

# Load the character matrix from the file
file_path = "./data/day06.txt"
matrix = read_matrix(file_path)

new_matrix = matrix.copy()

pos = np.where(matrix == "^")
dir = "up"
row, col = pos[0][0], pos[1][0]

rows, cols = np.where(matrix == "#")
obs = pd.DataFrame({"row": rows, "col": cols}).sort_values(["row", "col"])

in_map = True

while in_map:
    try:
        if dir == "up":
            mask_path = (obs["row"] < row) & (obs["col"] == col)
            obs_in_path = obs[mask_path]
            row_, col_ = obs_in_path.iloc[-1]
            row_ += 1
            dir = "right"
        elif dir == "right":
            mask_path = (obs["row"] == row) & (obs["col"] > col)
            obs_in_path = obs[mask_path]
            row_, col_ = obs_in_path.iloc[0]
            col_ -= 1
            dir = "down"
        elif dir == "down":
            mask_path = (obs["row"] > row) & (obs["col"] == col)
            obs_in_path = obs[mask_path]
            row_, col_ = obs_in_path.iloc[0]
            row_ -= 1
            dir = "left"
        elif dir == "left":
            mask_path = (obs["row"] == row) & (obs["col"] < col)
            obs_in_path = obs[mask_path]
            row_, col_ = obs_in_path.iloc[-1]
            col_ += 1
            dir = "up"
    except IndexError:
        if dir == "up":
            row_ = 1
        elif dir == "right":
            col_ = matrix.shape[1] - 1
        elif dir == "down":
            row_ = matrix.shape[0] - 1
        elif dir == "left":
            col_ = 1
        in_map = False

    src_row, dst_row = min(row, row_), max(row, row_)
    src_col, dst_col = min(col, col_), max(col, col_)
    path_row = list(range(src_row, dst_row + 1))
    path_col = list(range(src_col, dst_col + 1))
    new_matrix[path_row, path_col] = "X"
    row, col = row_, col_

print(new_matrix)
a, b = np.where(new_matrix == "X")
print(len(a))
