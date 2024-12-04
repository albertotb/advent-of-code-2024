import re
from operator import mul  # noqa

with open("./data/day03.txt", "r") as file:
    res = []
    flag = True
    for line in file:
        matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for m in matches:
            if m == "do()":
                flag = True
            elif m == "don't()":
                flag = False
            else:
                if flag:
                    res.append(eval(m))

print(sum(res))
