#!/usr/bin/env python3.9
def get_input():
    with open('input.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]

def get_most_common(numbers, pos):
    first_number = numbers[0]
    puzzle = [{"1": 0, "0": 0} for _ in first_number]

    for number in numbers:
        for i, digit in enumerate(number):
            puzzle[i][digit] += 1

    most_common = "1" if puzzle[pos]["1"] >= puzzle[pos]["0"] else "0"
    return [x for x in numbers if x[pos] == most_common]

def get_less_common(numbers, pos):
    first_number = numbers[0]
    puzzle = [{"1": 0, "0": 0} for _ in first_number]

    for number in numbers:
        for i, digit in enumerate(number):
            puzzle[i][digit] += 1

    less_common = "0" if puzzle[pos]["1"] >= puzzle[pos]["0"] else "1"
    return [x for x in numbers if x[pos] == less_common]


def find_oxygen(numbers):
    i = 0
    nums = numbers
    while len(nums) > 1:
        nums = get_most_common(nums, i)
        i += 1

    return int("0b" + nums[0], 0)

def find_co2(numbers):
    i = 0
    nums = numbers
    while len(nums) > 1:
        nums = get_less_common(nums, i)
        i += 1

    return int("0b" + nums[0], 0)

def solve():
    _input = get_input()
    ox = find_oxygen(_input)
    co2 = find_co2(_input)
    print(ox * co2)

if __name__ == "__main__":
    solve()
