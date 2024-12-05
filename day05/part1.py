def process_input():
    with open("input.txt") as f:
        ordering_rules, pages_to_produce = f.read().split("\n\n")
        ordering_rules = [[int(i) for i in j.split("|")] for j in ordering_rules.splitlines()]
        pages_to_produce = [[int(i) for i in j.split(",")] for j in pages_to_produce.splitlines()]
        return ordering_rules, pages_to_produce


def solve():
    total = 0
    ordering_rules, pages_to_produce = process_input()
    for page in pages_to_produce:
        for rule in ordering_rules:
            if rule[0] in page and rule[1] in page:
                if page.index(rule[0]) > page.index(rule[1]):
                    break
        else:
            middle = len(page) // 2
            total += page[middle]
    print(total)


if __name__ == "__main__":
    solve()
