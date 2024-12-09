def process_input():
    with open("input.txt") as f:
        return f.read()


def print_disk(disk_space):
    for d in disk_space:
        print(d, end='')
    print()


def solve():
    disk_map = process_input()
    disk_space = []
    total = 0
    for i in range(0, len(disk_map), 2):
        for j in range(int(disk_map[i])):
            disk_space.append(i // 2)
        if i < len(disk_map) - 2:
            for k in range(int(disk_map[i + 1])):
                disk_space.append('.')

    start = 0
    end = len(disk_space) - 1
    while start < end:
        if disk_space[start] != '.':
            start += 1
        elif disk_space[end] == '.':
            end -= 1
        else:
            disk_space[start], disk_space[end] = disk_space[end], disk_space[start]
            start += 1
            end -= 1

    for i in range(len(disk_space)):
        if disk_space[i] == '.':
            break
        else:
            total += i * disk_space[i]
    print(total)


if __name__ == "__main__":
    solve()
