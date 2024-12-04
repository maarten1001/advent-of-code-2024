import re


def process_input():
    with open("input.txt") as f:
        return f.read()


def solve():
    memory = process_input()
    total = 0
    enabled = True
    instructions = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", memory)
    for instr in instructions:
        if instr == "do()":
            enabled = True
        elif instr == "don't()":
            enabled = False
        else:
            if enabled is True:
                instr = re.findall(r"\d+", instr)
                total += int(instr[0]) * int(instr[1])
    print(total)


if __name__ == "__main__":
    solve()
