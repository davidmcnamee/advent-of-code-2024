from tqdm import tqdm


def is_valid(total, nums):
    n = len(nums)
    for i in range(3**n):
        binary = bin(i)[2:].zfill(n)
        cur = nums[0]
        for x, j in enumerate(nums[1:]):
            if binary[x] == "0":
                cur += j
            else:
                cur *= j
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
