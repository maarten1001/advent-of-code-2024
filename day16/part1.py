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


def find_neighbours(grid, x, y, direction):
    neighbours = []
    if direction == 'E':
        if grid[y - 1][x] != '#':
            neighbours.append((x, y - 1, 1001, 'N'))
        if grid[y + 1][x] != '#':
            neighbours.append((x, y + 1, 1001, 'S'))
        if grid[y][x + 1] != '#':
            neighbours.append((x + 1, y,    1, 'E'))
        if grid[y][x - 1] != '#':
            neighbours.append((x - 1, y, 2001, 'W'))
    elif direction == 'S':
        if grid[y - 1][x] != '#':
            neighbours.append((x, y - 1, 2001, 'N'))
        if grid[y + 1][x] != '#':
            neighbours.append((x, y + 1,    1, 'S'))
        if grid[y][x + 1] != '#':
            neighbours.append((x + 1, y, 1001, 'E'))
        if grid[y][x - 1] != '#':
            neighbours.append((x - 1, y, 1001, 'W'))
    elif direction == 'W':
        if grid[y - 1][x] != '#':
            neighbours.append((x, y - 1, 1001, 'N'))
        if grid[y + 1][x] != '#':
            neighbours.append((x, y + 1, 1001, 'S'))
        if grid[y][x + 1] != '#':
            neighbours.append((x + 1, y, 2001, 'E'))
        if grid[y][x - 1] != '#':
            neighbours.append((x - 1, y,    1, 'W'))
    elif direction == 'N':
        if grid[y - 1][x] != '#':
            neighbours.append((x, y - 1,    1, 'N'))
        if grid[y + 1][x] != '#':
            neighbours.append((x, y + 1, 2001, 'S'))
        if grid[y][x + 1] != '#':
            neighbours.append((x + 1, y, 1001, 'E'))
        if grid[y][x - 1] != '#':
            neighbours.append((x - 1, y, 1001, 'W'))
    return neighbours


def dijkstra(grid, start, end):
    q = []
    dist = [[[-1 for _ in range(4)] for _ in y] for y in grid]
    # label root as explored
    start_x, start_y, direction = start
    dist[start_y][start_x][direction] = 0
    print(dist)
    q.append(start)
    while len(q) != 0:
        vx, vy, direction = q.pop(0)
        if (vx, vy) == end:
            return dist[vy][vx]
        for wx, wy, direction in find_neighbours(grid, vx, vy, direction):
            if dist[wy][wx] == -1:
                dist[wy][wx] = dist[vy][vx] + 1
                q.append((wx, wy))


def solve():
    grid = process_input()
    start_x, start_y = find_char(grid, 'S')
    end = find_char(grid, 'E')
    direction = 'E'
    start = (start_x, start_y, direction)
    print_grid(grid)
    print(start)
    print(end)
    dijkstra(grid, start, end)


if __name__ == "__main__":
    solve()
