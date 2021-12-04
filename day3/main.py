#!/usr/bin/env python3.9
def get_input():
    with open('input.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]


def solve():
    input = get_input()

    first_number = input[0]
    puzzle = [{"1": 0, "0": 0} for _ in first_number]

    for number in input:
        for i, digit in enumerate(number):
            puzzle[i][digit] += 1

    gamma = ""

    for position in puzzle:
        gamma += "1" if position["1"] > position["0"] else "0"

    def counter(x):
        return "1" if x == "0" else "0"
    epsilon = "".join(map(counter, list(gamma)))

    gamma = "0b" + gamma
    epsilon = "0b" + epsilon

    print(int(gamma, 0) * int(epsilon, 0))


if __name__ == "__main__":
    solve()
