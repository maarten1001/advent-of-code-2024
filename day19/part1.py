def process_input():
    with open("input.txt") as f:
        towels, designs = f.read().split("\n\n")
        towels = towels.split(", ")
        designs = designs.splitlines()
        return towels, designs


def find_design(design, towels):
    if design in towels:
        return True
    else:
        for towel in towels:
            if design.startswith(towel):
                new_design = design[len(towel):]
                if find_design(new_design, towels):
                    return True
        return False


def solve():
    towels, designs = process_input()
    total = 0
    for design in designs:
        if find_design(design, towels):
            total += 1

    print(total)


if __name__ == "__main__":
    solve()
