def process_input():
    with open("input.txt") as f:
        warehouse, movements = f.read().split("\n\n")
        warehouse = warehouse.splitlines()
        grid = [[x for x in y] for y in warehouse]
        movements = movements.replace("\n", "")
        return grid, movements


def print_grid(grid):
    broken = False
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end='')
            if grid[y][x] == '[' and grid[y][x + 1] != ']' or grid[y][x - 1] != '[' and grid[y][x] == ']':
                broken = True
        print()
    print()
    if broken:
        exit(1)


def find_char(grid, char):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                return x, y
    return -1, -1


def make_it_wide(grid):
    wide = [['.' for _ in range(2 * len(grid[0]))] for _ in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '#':
                wide[y][2 * x] = '#'
                wide[y][2 * x + 1] = '#'
            elif grid[y][x] == 'O':
                wide[y][2 * x] = '['
                wide[y][2 * x + 1] = ']'
            elif grid[y][x] == '@':
                wide[y][2 * x] = '@'
    return wide


def move(grid, x, y, direction, execute):
    if grid[y][x] == '.':
        return True
    if grid[y][x] == '#':
        return False
    if direction == '^':
        if grid[y][x] == '@' and move(grid, x, y - 1, direction, execute) is True:
            if execute is True:
                grid[y - 1][x] = grid[y][x]
                grid[y][x] = '.'
            return True
        elif grid[y][x] == '[' and move(grid, x, y - 1, direction, execute) and move(grid, x + 1, y - 1, direction, execute):
            if execute is True:
                grid[y - 1][x] = grid[y][x]
                grid[y][x] = '.'
                grid[y - 1][x + 1] = grid[y][x + 1]
                grid[y][x + 1] = '.'
            return True
        elif grid[y][x] == ']' and move(grid, x - 1, y - 1, direction, execute) and move(grid, x, y - 1, direction, execute):
            if execute is True:
                grid[y - 1][x - 1] = grid[y][x - 1]
                grid[y][x - 1] = '.'
                grid[y - 1][x] = grid[y][x]
                grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == '>':
        if move(grid, x + 1, y, direction, execute) is True:
            if execute is True:
                grid[y][x + 1] = grid[y][x]
                grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == 'v':
        if grid[y][x] == '@' and move(grid, x, y + 1, direction, execute) is True:
            if execute is True:
                grid[y + 1][x] = grid[y][x]
                grid[y][x] = '.'
            return True
        elif grid[y][x] == '[' and move(grid, x, y + 1, direction, execute) and move(grid, x + 1, y + 1, direction, execute):
            if execute is True:
                grid[y + 1][x] = grid[y][x]
                grid[y][x] = '.'
                grid[y + 1][x + 1] = grid[y][x + 1]
                grid[y][x + 1] = '.'
            return True
        elif grid[y][x] == ']' and move(grid, x - 1, y + 1, direction, execute) and move(grid, x, y + 1, direction, execute):
            if execute is True:
                grid[y + 1][x - 1] = grid[y][x - 1]
                grid[y][x - 1] = '.'
                grid[y + 1][x] = grid[y][x]
                grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == '<':
        if move(grid, x - 1, y, direction, execute) is True:
            if execute is True:
                grid[y][x - 1] = grid[y][x]
                grid[y][x] = '.'
            return True
        else:
            return False
    else:
        print(f"Unrecognized direction {direction}")
        exit(1)


def solve():
    grid, movements = process_input()
    grid = make_it_wide(grid)
    robot = '@'
    x, y = find_char(grid, robot)
    print("Initial state:")
    print_grid(grid)

    for direction in movements:
        print(f"Move {direction}:")
        if move(grid, x, y, direction, False) is True:
            move(grid, x, y, direction, True)
            if direction == '^':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == 'v':
                y += 1
            elif direction == '<':
                x -= 1
        # print_grid(grid)

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == '[':
                total += 100 * y + x
    print(total)


if __name__ == "__main__":
    solve()
