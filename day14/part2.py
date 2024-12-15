import re
import png


def process_input():
    with open("input.txt") as f:
        robot_list = f.read().splitlines()
        robots = []
        for i in range(len(robot_list)):
            numbers_list = re.findall(r"-?\d+", robot_list[i])
            robots.append([int(n) for n in numbers_list])
        return robots


def print_grid(robots, width, height):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for r in robots:
        grid[r[1]][r[0]] += 1
    for i in grid:
        for j in i:
            if j == 0:
                print(".", end='')
            else:
                print(j, end='')
        print()
    print()


def write_png(robots, width, height, s):
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for r in robots:
        grid[r[1]][r[0]] = 255

    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            row = row + (grid[y][x], grid[y][x], grid[y][x])
        img.append(row)
    with open(str(s) + '.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def step(robots, width, height):
    for i in range(len(robots)):
        robots[i][0] = (robots[i][0] + robots[i][2]) % width
        robots[i][1] = (robots[i][1] + robots[i][3]) % height


def solve():
    robots = process_input()
    width = 101
    height = 103
    print("Initial state:")
    print_grid(robots, width, height)
    write_png(robots, width, height, 0)
    start = 1
    # after generating 1000 images, we notice two interesting patterns:
    # a vertical alignment at (index % width) == 23
    # a horizontal alignment at (index % height) == 89
    # so let's only print these images:
    for s in range(start, start + (width * height)):
        step(robots, width, height)
        if (s % width) == 23 and (s % height) == 89:
            write_png(robots, width, height, s)


if __name__ == "__main__":
    solve()
