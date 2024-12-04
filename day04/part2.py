def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[i for i in j] for j in lines]
        return grid


def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end='')
        print()
    print()


def find_x_mas(grid, x, y):
    if grid[y][x] != "A":
        return False

    string = grid[y - 1][x - 1] + grid[y - 1][x + 1] + grid[y + 1][x + 1] + grid[y + 1][x - 1]
    print(string)
    if string in ["MMSS", "SMMS", "SSMM", "MSSM"]:
        return True
    else:
        return False


def solve():
    grid = process_input()
    total = 0
    print_grid(grid)
    # as we work from the middle A, we can skip all edges
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            total += find_x_mas(grid, j, i)
    print(total)


if __name__ == "__main__":
    solve()
