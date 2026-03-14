import numpy as np
import pandas as pd

with open("./data/day09_test.txt") as file:
    data = file.read().strip()

array = np.array(list(map(int, data)))

used = pd.Series(array[0::2])
free = array[1::2]

print(used)

# La lista de huecos se puede actualizar!
res = {}
for id1, u1, f in zip(used.index, used.values, free):
    print(id1, u1, f)
    # Si no hay mas espacio y los punteros por la
    # izquierda y derecha se van a cruzar,
    # simplemente añadimos los bloques restantes
    # if (right - f) < (left + u):
    #     result.append(ids[left:right])
    #     break

    res[id1] = int(u1)

    for id2, u2 in used[id1 + 1 :][::-1].items():
        if u2 <= f:
            res[id2] = int(u2)
            if (f - u2) > 0:
                res[-(id1 + 1)] = int(f) - int(u2)
            break
    else:
        res[-(id1 + 1)] = int(f)

r = pd.Series(res)

print(r)

ids = np.repeat(r.index, r.values)
print(f"IDs: {ids}")
print(f"IDs size: {ids.size}")

# res = np.concatenate(result)
# print("".join(res.astype(str)))
# print(f"Result size: {res.size}")

# print((res * np.arange(res.size)).sum())
