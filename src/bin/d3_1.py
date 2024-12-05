# mull it over (part 1)
import re


def main():
    with open("inputs/d3") as f:
        raw_data = f.read()
    total = 0
    for match in re.finditer(r"mul\((\d+),(\d+)\)", raw_data):
        a, b = match.groups()
        total += int(a) * int(b)
    print(total)


if __name__ == "__main__":
    main()
