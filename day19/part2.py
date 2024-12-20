def process_input():
    with open("test1.txt") as f:
        towels, designs = f.read().split("\n\n")
        towels = towels.split(", ")
        designs = designs.splitlines()
        return towels, designs


def find_design(design, towels, depth=0):
    if design == "u":
        print(f"find_design at depth {depth} with design {design}")
    if len(design) == 0:
        return 1
    else:
        total = 0
        for towel in towels:
            if design.startswith(towel):
                # print(f"= {towel}")
                new_design = design[len(towel):]
                total += find_design(new_design, towels, depth + 1)
        return total


def solve():
    towels, designs = process_input()
    print(towels)
    print(designs)
    total = 0
    for design in designs:
        print(design)
        subtotal = find_design(design, towels)
        print(subtotal)
        total += subtotal
        print()

    print(total)


if __name__ == "__main__":
    solve()
