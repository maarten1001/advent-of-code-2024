def process_input():
    with open("input.txt") as f:
        entries = f.read().splitlines()
        list1 = []
        list2 = []
        for e in entries:
            e = e.split("   ")
            list1.append(int(e[0]))
            list2.append(int(e[1]))
        return list1, list2


def solve():
    list1, list2 = process_input()
    list1.sort()
    list2.sort()
    total = 0
    for i in range(0, len(list1)):
        total += abs(list1[i] - list2[i])
    print(total)


if __name__ == "__main__":
    solve()
