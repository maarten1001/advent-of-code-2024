def process_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def apply_operators(numbers, results, op="+", i=0, total=0):
    if i == 0:
        total = numbers[i]
    else:
        if op == "+":
            total += numbers[i]
        elif op == "*":
            total *= numbers[i]
        else:
            print(f"Undefined operator {op}")
            exit(1)

    if i == len(numbers) - 1:
        results.append(total)
    else:
        apply_operators(numbers, results, "+", i + 1, total)
        apply_operators(numbers, results, "*", i + 1, total)


def solve():
    total = 0
    equations = process_input()
    for line in equations:
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = [int(i) for i in numbers.split()]
        results = []
        apply_operators(numbers, results)
        if test_value in results:
            total += test_value
    print(total)


if __name__ == "__main__":
    solve()
