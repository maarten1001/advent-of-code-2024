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
        a_max = min(prize_x // a_x, prize_y // a_y, 100)
        b_max = min(prize_x // b_x, prize_y // b_y, 100)
        number_of_tokens = 999
        for a in range(a_max + 1):
            for b in range(b_max + 1):
                if a * a_x + b * b_x == prize_x and a * a_y + b * b_y == prize_y:
                    number_of_tokens = min(3 * a + 1 * b, number_of_tokens)
        if number_of_tokens != 999:
            total += number_of_tokens
    print(total)


if __name__ == "__main__":
    solve()
