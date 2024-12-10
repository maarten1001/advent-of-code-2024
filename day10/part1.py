def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[int(x) for x in y] for y in lines]
        return grid


def print_grid(grid):
    for i in grid:
        for j in i:
            print(f" {j}", end='')
        print()
    print()


def mark_the_trail(grid, scores, x, y, trailheads):
    height = grid[y][x]
    if height == 0 and (x,y) not in trailheads:
        scores[y][x] += 1
        trailheads.append((x,y))
    else:
        if y < len(grid) - 1 and grid[y + 1][x] == height - 1:
             mark_the_trail(grid, scores, x, y + 1, trailheads)
        if y > 0 and grid[y - 1][x] == height - 1:
            mark_the_trail(grid, scores, x, y - 1, trailheads)
        if x < len(grid[0]) - 1 and grid[y][x + 1] == height - 1:
            mark_the_trail(grid, scores, x + 1, y, trailheads)
        if x > 0 and grid[y][x - 1] == height - 1:
            mark_the_trail(grid, scores, x - 1, y, trailheads)


def solve():
    grid = process_input()
    scores = [[0 for _ in y] for y in grid]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 9:
                trailheads = []
                mark_the_trail(grid, scores, x, y, trailheads)

    print(sum([sum(x) for x in scores]))


if __name__ == "__main__":
    solve()
