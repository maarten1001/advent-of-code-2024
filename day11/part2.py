def process_input():
    with open("input.txt") as f:
        stones = f.read().split()
        stones_dict = {}
        for s in stones:
            stones_dict.update({int(s): 1})
        return stones_dict


def blink(before):
    after = before.copy()
    for number, count in before.items():
        after[number] = after[number] - before[number]
        if number == 0:
            after[1] = after.get(1, 0) + count
        else:
            stone = str(number)
            if len(stone) % 2 == 0:
                length = len(stone)
                left = int(stone[:length // 2])
                right = int(stone[length // 2:])
                after[right] = after.get(right, 0) + count
                after[left] = after.get(left, 0) + count
            else:
                product = number * 2024
                after[product] = after.get(product, 0) + count
    return after


def solve():
    stones = process_input()
    for i in range(75):
        stones = blink(stones)

    total = 0
    for number, count in stones.items():
        total += count
    print(total)


if __name__ == "__main__":
    solve()
