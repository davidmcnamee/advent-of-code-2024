from typing import Generator


def safe_without_dampener(report: list[int]) -> bool:
    def get_data() -> Generator[tuple[bool, bool], None, None]:
        for x, y in zip(report[:-1], report[1:]):
            yield (x < y, 1 <= abs(x - y) <= 3)

    is_asc, is_bounded = zip(*get_data())
    return (all(is_asc) or not any(is_asc)) and all(is_bounded)


def is_safe(report: list[int]) -> bool:
    for i in range(len(report)):
        if safe_without_dampener(report[:i] + report[i + 1 :]):
            return True
    return False


def main():
    with open("inputs/d2_1") as f:
        raw_reports = f.read().strip().split("\n")

    safe_count = 0
    for raw_report in raw_reports:
        report = [int(x) for x in raw_report.split(" ")]
        safe_count += is_safe(report)
    print(safe_count)


if __name__ == "__main__":
    main()
