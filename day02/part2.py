def process_input():
    with open("input.txt") as f:
        return f.read().splitlines()


def is_report_safe(report):
    if report[0] < report[1]:
        # increasing
        for j in range(0, len(report) - 1):
            if 1 <= report[j + 1] - report[j] <= 3:
                continue
            return False
        else:
            return True
    elif report[1] < report[0]:
        # decreasing
        for j in range(0, len(report) - 1):
            if 1 <= report[j] - report[j + 1] <= 3:
                continue
            return False
        else:
            return True
    else:
        # unsafe
        return False


def solve():
    reports = process_input()
    total = 0
    for i in range(0, len(reports)):
        report = [int(x) for x in reports[i].split()]
        if is_report_safe(report):
            total += 1
        else:
            for j in range(0, len(report)):
                report2 = report.copy()
                report2.pop(j)
                if is_report_safe(report2):
                    total += 1
                    break
    print(total)


if __name__ == "__main__":
    solve()
