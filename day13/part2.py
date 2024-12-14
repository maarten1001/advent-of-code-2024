import re


def process_input():
    with open("input.txt") as f:
        machine_list = f.read().split("\n\n")
        claw_machines = []
        for i in range(len(machine_list)):
            numbers_list = re.findall(r"\d+", machine_list[i])
            claw_machines.append([int(n) for n in numbers_list])
        return claw_machines


def solve():
    claw_machines = process_input()
    total = 0
    for machine in claw_machines:
        a_x, a_y, b_x, b_y, prize_x, prize_y = machine
        prize_x += 10000000000000
        prize_y += 10000000000000
        print("=============================")
        print()
        print(f"{a_x}A + {b_x}B = {prize_x}")
        print(f"{a_y}A + {b_y}B = {prize_y}")
        print()

        # multiply to make A equal for both equations
        a1 = a_x * a_y
        b1 = b_x * a_y
        p1 = prize_x * a_y
        print(f"{a1}A + {b1}B = {p1}")
        a2 = a_y * a_x
        b2 = b_y * a_x
        p2 = prize_y * a_x
        print(f"{a2}A + {b2}B = {p2}")
        print()

        # subtract the smallest equation from the largest
        if b1 > b2:
            b3 = b1 - b2
            p3 = p1 - p2
        else:
            b3 = b2 - b1
            p3 = p2 - p1
        print(f"{b3}B = {p3}")
        print()

        # check if we have an integer solution
        if p3 % b3 != 0:
            print(f"Cannot divide by b => no prize")
            print()
            continue
        b = p3 // b3
        print(f"B = {b}")
        print()

        # fill out b in one of the original equations
        print(f"{a_x}A + {b_x * b} = {prize_x}")
        print()
        a4 = prize_x - (b_x * b)
        print(f"{a_x}A = {a4}")
        print()

        # check if we have an integer solution
        if a4 % a_x != 0:
            print(f"Cannot divide by a => no prize")
            print()
            continue
        a = a4 // a_x
        print(f"A = {a}")
        print()

        # count the tokens
        total += 3 * a + b
    print(total)


if __name__ == "__main__":
    solve()
