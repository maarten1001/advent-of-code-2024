def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[x for x in y] for y in lines]
        return grid


def print_grid(grid):
    for y in grid:
        for x in y:
            print(x, end='')
        print()
    print()


def find_char(grid, char):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                return x, y
    return -1, -1


def solve():
    start_grid = process_input()
    guard = '^'
    obstr = 'O'
    x, y = find_char(start_grid, guard)
    start_x = x
    start_y = y
    start_guard = guard
    total = 0
    for obstr_y in range(len(start_grid)):
        for obstr_x in range(len(start_grid[0])):
            if obstr_x == start_x and obstr_y == start_y:
                continue
            print(obstr_x, obstr_y)
            guard = start_guard
            x = start_x
            y = start_y
            grid = [x[:] for x in start_grid]
            grid[obstr_y][obstr_x] = obstr
            been_there = []
            while True:
                been_there.append((guard, x, y))
                grid[y][x] = 'X'
                if guard == '^':
                    if y == 0:
                        break
                    if grid[y - 1][x] == '#' or grid[y - 1][x] == 'O':
                        guard = '>'
                    else:
                        y -= 1
                elif guard == '>':
                    if x == len(grid[0]) - 1:
                        break
                    if grid[y][x + 1] == '#' or grid[y][x + 1] == 'O':
                        guard = 'V'
                    else:
                        x += 1
                elif guard == 'V':
                    if y == len(grid) - 1:
                        break
                    if grid[y + 1][x] == '#' or grid[y + 1][x] == 'O':
                        guard = '<'
                    else:
                        y += 1
                elif guard == '<':
                    if x == 0:
                        break
                    if grid[y][x - 1] == '#' or grid[y][x - 1] == 'O':
                        guard = '^'
                    else:
                        x -= 1

                if (guard, x, y) in been_there:
                    # we are in a loop
                    total += 1
                    break
    print(total)


if __name__ == "__main__":
    solve()
