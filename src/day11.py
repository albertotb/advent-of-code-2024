initial = "0 1 10 99 999"
initial = "125 17"
# initial = "20 82084 1650 3 346355 363 7975858 0"

stones = initial.split(" ")
print(stones)


def apply_rules(x):
    res = []
    if int(x) == 0:
        res.append("1")
    elif (s := len(x)) % 2 == 0:
        res.append(str(int(x[: (s // 2)])))
        res.append(str(int(x[(s // 2) :])))
    else:
        res.append(str(int(x) * 2024))
    return res


cache = {}
total = 0
for i in range(25):
    for x in stones:
        if x in cache:
            total += cache[x]
        else:
            new_stones = apply_rules(x)
            print(new_stones)
            cache[x] = len(new_stones)
            total += len(new_stones)

            stones.extend(new_stones)

print(total)
