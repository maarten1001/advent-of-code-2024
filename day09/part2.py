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

    end_length = 1
    for end in range(len(disk_space) - 1, -1, -1):
        if disk_space[end] == '.':
            continue
        if disk_space[end - 1] == disk_space[end]:
            end_length += 1
            continue

        for start in range(0, end):
            start_length = 1
            if disk_space[start] != '.':
                continue

            start_i = start
            while disk_space[start_i + 1] == disk_space[start_i]:
                start_length += 1
                start_i += 1
            if end_length <= start_length:
                for i in range(end_length):
                    disk_space[start + i] = disk_space[end + i]
                    disk_space[end + i] = '.'
                break
            else:
                start += start_length
        end_length = 1

    for i in range(len(disk_space)):
        if disk_space[i] != '.':
            total += i * disk_space[i]
    print(total)


if __name__ == "__main__":
    solve()
