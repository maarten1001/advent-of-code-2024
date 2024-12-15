import re


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


def step(robots, width, height):
    for i in range(len(robots)):
        robots[i][0] = (robots[i][0] + robots[i][2]) % width
        robots[i][1] = (robots[i][1] + robots[i][3]) % height


def solve():
    robots = process_input()
    width = 101
    height = 103
    print_grid(robots, width, height)
    for _ in range(100):
        step(robots, width, height)
        print_grid(robots, width, height)

    q1 = q2 = q3 = q4 = 0
    for robot in robots:
        if robot[0] < width // 2:
            if robot[1] < height // 2:
                q1 += 1
            if robot[1] > height // 2:
                q3 += 1
        else:
            if robot[0] > width // 2:
                if robot[1] < height // 2:
                    q2 += 1
                if robot[1] > height // 2:
                    q4 += 1
    print(q1 * q2 * q3 * q4)


if __name__ == "__main__":
    solve()
