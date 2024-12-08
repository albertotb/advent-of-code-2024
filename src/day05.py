from collections import defaultdict, deque

import pandas as pd


def topological_sort(rules):
    # Step 1: Build the graph
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    nodes = set()

    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        nodes.add(x)
        nodes.add(y)

    # Initialize in-degrees for all nodes
    for node in nodes:
        if node not in in_degree:
            in_degree[node] = 0

    # Step 2: Find all nodes with in-degree 0
    queue = deque([node for node in nodes if in_degree[node] == 0])

    # Step 3: Perform topological sort
    result = []
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If result does not contain all nodes, there's a cycle
    if len(result) != len(nodes):
        raise ValueError("The rules contain a cycle, so no valid order exists.")

    return result


# Esto funciona para el caso de prueba pero no para el caso real
# order = data_series.index.nunique() - data_series.groupby(level=0).size()

basename = "data/day05"

# Read the file into a pandas Series
file_path = f"{basename}_rules.txt"
data_series = pd.read_csv(file_path, sep="|", header=None, index_col=0).squeeze(
    "columns"
)

total = 0
total_incorrect = 0
with open(f"{basename}.txt", "r") as file:
    for line in file:
        # Si no podemos mapear un numero es que no aparece a la izquierda
        # de una regla y por tanto todos tienen que ser menor que el
        s = pd.Series(line.strip().split(",")).astype(int)

        rules = list(zip(data_series[s].index, data_series[s]))
        order = topological_sort(rules)
        order = pd.Series(range(len(order)), index=order)

        s_order = s.map(order).fillna(len(order))
        if (s_order.diff().dropna() > 0).all():
            total += s[len(s) // 2]
        else:
            s_correct = s[s_order.sort_values().index].reset_index(drop=True)
            total_incorrect += s_correct[len(s) // 2]

print(total)
print(total_incorrect)
