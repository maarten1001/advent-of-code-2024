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
    total = 0
    for number in list1:
        total += number * list2.count(number)
    print(total)


if __name__ == "__main__":
    solve()
