# print queue (part 1)
def is_valid(ordering: list[int], rules: set[tuple[int, int]]) -> bool:
    for i, x in enumerate(ordering):
        for y in ordering[i + 1 :]:
            if (y, x) in rules:
                return False
    return True


def main():
    with open("inputs/d5") as f:
        data = f.read().strip().splitlines()

    empty_line_index = data.index("")
    raw_rules = data[:empty_line_index]
    orderings = data[empty_line_index + 1 :]

    rules = set()
    for rule in raw_rules:
        x, y = rule.split("|")
        rules.add((int(x), int(y)))

    total = 0
    for raw_ordering in orderings:
        ordering = [int(x) for x in raw_ordering.split(",")]
        if not is_valid(ordering, rules):
            continue
        total += ordering[len(ordering) // 2]
    print(total)


if __name__ == "__main__":
    main()
