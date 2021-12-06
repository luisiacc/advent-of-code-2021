#!/usr/bin/env python3.9

from collections import defaultdict


def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return f.read()


DAYS = 256


def main():
    lanterns = list(map(int, get_input().split(",")))

    nums = defaultdict(int)
    for n in lanterns:
        if n not in nums:
            nums[n] = 0
        nums[n] += 1

    for d in range(DAYS):
        newnums = defaultdict(int)
        for n, cnt in nums.items():
            if n == 0:
                newnums[6] += cnt
                newnums[8] += cnt
            else:
                newnums[n - 1] += cnt
        nums = newnums

    print(sum(nums.values()))


if __name__ == "__main__":
    main()
