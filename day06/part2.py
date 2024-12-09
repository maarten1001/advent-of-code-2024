def process_input():
    with open("test1.txt") as f:
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


def step(grid, guard, x, y, off_the_grid):
    off_the_grid = False
    if guard == '^':
        if y == 0:
            off_the_grid = True
        if grid[y - 1][x] == '#':
            guard = '>'
            if x == len(grid[0]) - 1:
                off_the_grid = True
        else:
            y -= 1
    elif guard == '>':
        if x == len(grid[0]) - 1:
            off_the_grid = True
        if grid[y][x + 1] == '#':
            guard = 'V'
            if y == len(grid) - 1:
                off_the_grid = True
        else:
            x += 1
    elif guard == 'V':
        if y == len(grid) - 1:
            off_the_grid = True
        if grid[y + 1][x] == '#':
            guard = '<'
            if x == 0:
                off_the_grid = True
        else:
            y += 1
    elif guard == '<':
        if x == 0:
            off_the_grid = True
        if grid[y][x - 1] == '#':
            guard = '^'
            if y == 0:
                off_the_grid = True
        else:
            x -= 1

    return grid, guard, x, y, off_the_grid


def look_ahead(grid, guard, x, y):
    off_the_grid = False
    char = ''
    if guard == '^':
        if y == 0:
            off_the_grid = True
        else:
            char = grid[y - 1][x]
    elif guard == '>':
        if x == len(grid[0]) - 1:
            off_the_grid = True
        else:
            char = grid[y][x + 1]
    elif guard == 'V':
        if y == len(grid) - 1:
            off_the_grid = True
        else:
            char = grid[y + 1][x]
    elif guard == '<':
        if x == 0:
            off_the_grid = True
        else:
            char = grid[y][x - 1]

    return off_the_grid, char


def solve():
    start_grid = process_input()
    guard = '^'
    # obstr = 'O'
    x, y = find_char(start_grid, guard)
    start_x = x
    start_y = y
    start_guard = guard
    total = 0
    max_steps = 1
    while True:
        grid = [x[:] for x in start_grid]
        guard = start_guard
        x = start_x
        y = start_y
        off_the_grid = False
        for i in range(max_steps):
            grid, guard, x, y, off_the_grid = step(grid, guard, x, y, off_the_grid)
        if off_the_grid is True:
            break
        # grid[obstr_y][obstr_x] = obstr
        been_there = []
        while True:
            been_there.append((guard, x, y))
            step(grid, guard, x, y, off_the_grid)

            if (guard, x, y) in been_there:
                # we are in a loop
                total += 1
                break

    print(total)


if __name__ == "__main__":
    solve()
