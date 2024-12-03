import re

def process_input():
    with open("input.txt") as f:
        return f.read()


def solve():
    memory = process_input()
    total = 0
    mul = re.findall(r"mul\(\d+,\d+\)", memory)
    print(mul)
    for m in mul:
        m = re.findall(r"\d+", m)
        print(m)
        total += int(m[0]) * int(m[1])
    print(total)


if __name__ == "__main__":
    solve()
