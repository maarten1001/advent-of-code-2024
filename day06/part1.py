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
    grid = process_input()
    guard = '^'
    x, y = find_char(grid, guard)
    while True:
        grid[y][x] = 'X'
        if guard == '^':
            if y == 0:
                break
            if grid[y - 1][x] == '#':
                guard = '>'
            else:
                y -= 1
        elif guard == '>':
            if x == len(grid[0]) - 1:
                break
            if grid[y][x + 1] == '#':
                guard = 'V'
            else:
                x += 1
        elif guard == 'V':
            if y == len(grid) - 1:
                break
            if grid[y + 1][x] == '#':
                guard = '<'
            else:
                y += 1
        elif guard == '<':
            if x == 0:
                break
            if grid[y][x - 1] == '#':
                guard = '^'
            else:
                x -= 1

    grid[y][x] = 'X'
    print(sum([x.count('X') for x in grid]))


if __name__ == "__main__":
    solve()
