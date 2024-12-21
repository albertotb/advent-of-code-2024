import numpy as np

with open("./data/day09.txt") as file:
    data = file.read().strip()

array = np.array(list(map(int, data)))

used = array[0::2]
free = array[1::2]

print(f"Used: {used}")
print(f"Free: {free}")

ids = np.repeat(np.arange(used.size), used)
print(f"IDs: {ids}")
print(f"IDs size: {ids.size}")

left = 0
right = ids.shape[0]
result = []
for u, f in zip(used, free):
    # Si no hay mas espacio y los punteros por la
    # izquierda y derecha se van a cruzar,
    # simplemente añadimos los bloques restantes
    if (right - f) < (left + u):
        result.append(ids[left:right])
        break

    # Blocks before the free space
    result.append(ids[left : left + u])
    # Blocks to move from the end to the free space
    result.append(ids[right - f : right][::-1])

    left = left + u
    right = right - f


res = np.concatenate(result)
# print("".join(res.astype(str)))
print(f"Result size: {res.size}")

print((res * np.arange(res.size)).sum())
