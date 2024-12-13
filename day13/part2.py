import re


def process_input():
    with open("test1.txt") as f:
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
        a_max = min(prize_x // a_x, prize_y // a_y)
        b_max = min(prize_x // b_x, prize_y // b_y)
        number_of_tokens = 99999999999999
        a = 0
        b = b_max
        while b >= 0:
            print(f"a: {a}, b: {b}, number of tokens: {number_of_tokens}")
            print(a * a_x + b * b_x)
            print(a * a_y + b * b_y)
            if (a * a_x + b * b_x == prize_x) and (a * a_y + b * b_y == prize_y):
                number_of_tokens = min(3 * a + 1 * b, number_of_tokens)
                b -= 1
            if (a * a_x + b * b_x > prize_x) or (a * a_y + b * b_y > prize_y):
                b -= 1
            elif (a * a_x + b * b_x < prize_x) and (a * a_y + b * b_y < prize_y):
                a += 1
                if a > a_max:
                    break
            input(total)
        if number_of_tokens != 99999999999999:
            total += number_of_tokens
    print(total)


if __name__ == "__main__":
    solve()
