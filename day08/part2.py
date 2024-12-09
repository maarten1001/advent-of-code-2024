def process_input():
    with open("input.txt") as f:
        lines = f.read().splitlines()
        grid = [[x for x in y] for y in lines]
        return grid


def print_grid(grid, antinodes):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                print(grid[y][x], end='')
            else:
                if antinodes[y][x] > 0:
                    print('#', end='')
                else:
                    print('.', end='')
        print()
    print()


def get_antennas(grid):
    antennas = []
    frequencies = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '.':
                antennas.append({
                    "frequency": grid[y][x],
                    "x": x,
                    "y": y
                })
                frequencies.add(grid[y][x])
    return antennas, frequencies


def solve():
    grid = process_input()
    antinodes = [[0 for _ in y] for y in grid]
    antennas, frequencies = get_antennas(grid)

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            if antennas[i]["frequency"] != antennas[j]["frequency"]:
                continue
            antinodes[antennas[i]["y"]][antennas[i]["x"]] = 1
            antinodes[antennas[j]["y"]][antennas[j]["x"]] = 1

            diff_x = antennas[i]["x"] - antennas[j]["x"]
            diff_y = antennas[i]["y"] - antennas[j]["y"]

            if diff_x < 0:
                if diff_y < 0:
                    x1 = antennas[i]["x"] - abs(diff_x)
                    x2 = antennas[j]["x"] + abs(diff_x)
                    y1 = antennas[i]["y"] - abs(diff_y)
                    y2 = antennas[j]["y"] + abs(diff_y)
                else:
                    x1 = antennas[i]["x"] - abs(diff_x)
                    x2 = antennas[j]["x"] + abs(diff_x)
                    y1 = antennas[i]["y"] + abs(diff_y)
                    y2 = antennas[j]["y"] - abs(diff_y)
            else:
                if diff_y < 0:
                    x1 = antennas[j]["x"] - abs(diff_x)
                    x2 = antennas[i]["x"] + abs(diff_x)
                    y1 = antennas[j]["y"] + abs(diff_y)
                    y2 = antennas[i]["y"] - abs(diff_y)
                else:
                    x1 = antennas[j]["x"] - abs(diff_x)
                    x2 = antennas[i]["x"] + abs(diff_x)
                    y1 = antennas[j]["y"] - abs(diff_y)
                    y2 = antennas[i]["y"] + abs(diff_y)

            if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
                antinodes[y1][x1] = 1
            if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                antinodes[y2][x2] = 1

            while True:
                if diff_x < 0:
                    if diff_y < 0:
                        x1 = x1 - abs(diff_x)
                        y1 = y1 - abs(diff_y)
                    else:
                        x1 = x1 - abs(diff_x)
                        y1 = y1 + abs(diff_y)
                else:
                    if diff_y < 0:
                        x1 = x1 - abs(diff_x)
                        y1 = y1 + abs(diff_y)
                    else:
                        x1 = x1 - abs(diff_x)
                        y1 = y1 - abs(diff_y)

                if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
                    antinodes[y1][x1] = 1
                else:
                    break

            while True:
                if diff_x < 0:
                    if diff_y < 0:
                        x2 = x2 + abs(diff_x)
                        y2 = y2 + abs(diff_y)
                    else:
                        x2 = x2 + abs(diff_x)
                        y2 = y2 - abs(diff_y)
                else:
                    if diff_y < 0:
                        x2 = x2 + abs(diff_x)
                        y2 = y2 - abs(diff_y)
                    else:
                        x2 = x2 + abs(diff_x)
                        y2 = y2 + abs(diff_y)

                if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid):
                    antinodes[y2][x2] = 1
                else:
                    break

    print(sum([sum(x) for x in antinodes]))


if __name__ == "__main__":
    solve()
