def process_input():
    with open("input.txt") as f:
        stones = f.read().split()
        return [int(s) for s in stones]


def blink(stones):
    for i in range(len(stones) - 1, -1, -1):
        if stones[i] == 0:
            stones[i] = 1
        else:
            stone = str(stones[i])
            if len(stone) % 2 == 0:
                length = len(stone)
                left = int(stone[:length // 2])
                right = int(stone[length // 2:])
                # print(f"Splitting {stone} into {left} and {right}")
                stones[i] = right
                stones.insert(i, left)
            else:
                stones[i] *= 2024


def solve():
    stones = process_input()
    for i in range(25):
        blink(stones)
    print(len(stones))


if __name__ == "__main__":
    solve()
