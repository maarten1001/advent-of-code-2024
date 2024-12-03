def process_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def solve():
    reports = process_input()
    total = 0
    for i in range(0, len(reports)):
        report = [int(x) for x in reports[i].split()]
        if report[0] < report[1]:
            # increasing
            for j in range(0, len(report) - 1):
                if 1 <= report[j + 1] - report[j] <= 3:
                    continue
                break
            else:
                total += 1
        elif report[1] < report[0]:
            # decreasing
            for j in range(0, len(report) - 1):
                if 1 <= report[j] - report[j + 1] <= 3:
                    continue
                break
            else:
                total += 1
        else:
            # unsafe
            pass
    print(total)


if __name__ == "__main__":
    solve()
