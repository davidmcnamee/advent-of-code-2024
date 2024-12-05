# mull it over (part 2)
import re


def main():
    with open("inputs/d3") as f:
        raw_data = f.read()
    total = 0
    active = True
    for match in re.finditer(r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", raw_data):
        is_mul, a, b, is_do, is_dont = match.groups()
        if is_mul and active:
            total += int(a) * int(b)
        elif is_do:
            active = True
        elif is_dont:
            active = False
    print(total)


if __name__ == "__main__":
    main()
