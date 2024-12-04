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


def find_word(grid, x, y, word):
    count = 0
    if grid[y][x] != word[0]:
        return count

    for diffY in range(-1, 2):
        for diffX in range(-1, 2):
            for i in range(len(word)):
                xx = x + (i * diffX)
                yy = y + (i * diffY)
                if 0 <= yy < len(grid) and 0 <= xx < len(grid[0]):
                    if grid[yy][xx] == word[i]:
                        print(f"Found {word[i]} on {yy},{xx}")
                    else:
                        print(f"Not found {word[i]} at {yy},{xx}")
                        break
                else:
                    print(f"Walked off the grid at {yy},{xx}")
                    break
            else:
                print("== Word complete! ==")
                count += 1
    return count


def solve():
    word = "XMAS"
    grid = process_input()
    total = 0
    print_grid(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += find_word(grid, j, i, word)
    print(total)


if __name__ == "__main__":
    solve()
