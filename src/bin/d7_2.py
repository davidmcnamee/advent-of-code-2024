from tqdm import tqdm


# taken from google, it was a little slow (there's definitely a faster way) but <60s was good enough
def to_base_3(n):
    """Converts a decimal number to base 3."""
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        result = str(remainder) + result
    return result


def is_valid(total, nums):
    n = len(nums)
    for i in range(3**n):
        binary = to_base_3(i).zfill(n)
        cur = nums[0]
        for x, j in enumerate(nums[1:]):
            if binary[x] == "0":
                cur += j
            elif binary[x] == "1":
                cur *= j
            else:
                cur = int(str(cur) + str(j), 10)
            if cur > total:
                break
        if cur == total:
            return True
    return False


# raw_input = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""


def main():
    raw_input = open("inputs/d7").read()
    sum_amt = 0

    for line in tqdm(raw_input.splitlines()):
        total, nums = line.split(": ")
        total = int(total, 10)
        nums = [int(num, 10) for num in nums.split(" ")]
        if is_valid(total, nums):
            sum_amt += total
    print(sum_amt)


if __name__ == "__main__":
    main()
