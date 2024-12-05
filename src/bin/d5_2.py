# print queue (part 2)
from collections import defaultdict


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

    rules = process_rules(raw_rules)

    total = 0
    for raw_ordering in orderings:
        ordering = [int(x) for x in raw_ordering.split(",")]
        if is_valid(ordering, rules):
            continue
        ordering = topological_sort(rules, ordering)
        total += ordering[len(ordering) // 2]
    print(total)


def process_rules(raw_rules):
    # create rule set
    rules = set()
    for rule in raw_rules:
        x, y = rule.split("|")
        rules.add((int(x), int(y)))
    return rules


def topological_sort(rules, ordering):
    in_degree = defaultdict(int)
    rules_map = defaultdict(list)
    for x, y in rules:
        if not (x in ordering and y in ordering):
            continue
        if x not in in_degree:
            in_degree[x] = 0
        in_degree[y] += 1
        rules_map[x].append(y)

    result = []
    while next_layer := [x for x in in_degree if in_degree[x] == 0]:
        for x in next_layer:
            del in_degree[x]
        for y in rules_map[x]:
            in_degree[y] -= 1
        result.extend(next_layer)
    return result


if __name__ == "__main__":
    main()
