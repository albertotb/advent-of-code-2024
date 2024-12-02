import pandas as pd

# Read the file into a pandas DataFrame
df = pd.read_csv("./data/day01.txt", sep=r"\s+", header=None)
# df = pd.read_csv("./data/day01_test.txt", sep=r"\s+", header=None)

# Display the DataFrame
a = df[0].sort_values().reset_index(drop=True)
b = df[1].sort_values().reset_index(drop=True)

print((a - b).abs().sum())

weight = a.map(b.value_counts()).fillna(0)

print((a * weight).sum())
