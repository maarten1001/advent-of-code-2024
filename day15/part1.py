def process_input():
    with open("input.txt") as f:
        warehouse, movements = f.read().split("\n\n")
        warehouse = warehouse.splitlines()
        grid = [[x for x in y] for y in warehouse]
        movements = movements.replace("\n", "")
        return grid, movements


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


def move(grid, x, y, direction):
    if grid[y][x] == '.':
        return True
    if grid[y][x] == '#':
        return False
    if direction == '^':
        if move(grid, x, y - 1, direction) is True:
            grid[y - 1][x] = grid[y][x]
            grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == '>':
        if move(grid, x + 1, y, direction) is True:
            grid[y][x + 1] = grid[y][x]
            grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == 'v':
        if move(grid, x, y + 1, direction) is True:
            grid[y + 1][x] = grid[y][x]
            grid[y][x] = '.'
            return True
        else:
            return False
    elif direction == '<':
        if move(grid, x - 1, y, direction) is True:
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
    robot = '@'
    x, y = find_char(grid, robot)
    print("Initial state:")
    print_grid(grid)

    for direction in movements:
        if move(grid, x, y, direction) is True:
            if direction == '^':
                y -= 1
            elif direction == '>':
                x += 1
            elif direction == 'v':
                y += 1
            elif direction == '<':
                x -= 1
        # print(f"Move {direction}:")
        # print_grid(grid)

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'O':
                total += 100 * y + x
    print(total)


if __name__ == "__main__":
    solve()
