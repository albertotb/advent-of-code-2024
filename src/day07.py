def agg(target, numbers, debug):
    if len(numbers) == 1:
        # if int(numbers[0]) == target:
        #     print(f"{debug} = {target}")
        # else:
        #     print(debug)
        return int(numbers[0]) == int(target)
    else:
        if int(numbers[0]) > target:
            return False

        found = False
        for op in ("+", "*", "||"):
            debug_ = debug + f"{int(numbers[0])} {op} {int(numbers[1])}"
            if op == "||":
                res = eval(f"{int(numbers[0])}{int(numbers[1])}")
            else:
                res = eval(f"{int(numbers[0])} {op} {int(numbers[1])}")

            if agg(target, [res] + numbers[2:], debug=debug_):
                found = True
                break

        return found


file_path = "data/day07.txt"

total = 0
with open(file_path, "r") as file:
    for line in file:
        # print(line.strip())
        target, rest = line.strip().split(":")
        numbers = rest.split()
        if agg(int(target), numbers, debug=""):
            total += int(target)
        # print("\n")

print(total)
