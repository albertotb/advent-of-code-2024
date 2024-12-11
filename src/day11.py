initial = "0 1 10 99 999"
initial = "125 17"
initial = "20 82084 1650 3 346355 363 7975858 0"

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


def dfs(i, stone, res):
    if stone == "2":
        print(i)
        return i
    else:
        stones = apply_rules(stone)
        print(stones)
        for x in stones:
            print(x)
            res.append(dfs(i + 1, x, res))
    return res


# print(stones[0])
# res = []
# dfs(0, stones[0], res)

# print(res)


# is_2 = [-1] * len(stones)

stones = ["2"]

for i in range(75):
    res = []
    for x in stones:
        res.extend(apply_rules(x))
    stones = res

print(len(stones))
