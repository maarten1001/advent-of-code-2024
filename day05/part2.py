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
        was_already_sorted = True
        while True:
            # bubble sort
            keep_sorting = False
            for rule in ordering_rules:
                if rule[0] in page and rule[1] in page:
                    index0 = page.index(rule[0])
                    index1 = page.index(rule[1])
                    if index0 > index1:
                        was_already_sorted = False
                        keep_sorting = True
                        page[index0], page[index1] = page[index1], page[index0]
                        break
            if keep_sorting is False:
                break
        if was_already_sorted is False:
            middle = len(page) // 2
            total += page[middle]
    print(total)


if __name__ == "__main__":
    solve()
