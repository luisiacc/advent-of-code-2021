#!usr/bin/env python3.9
import itertools


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


table = {
    ")": 3,
    "(": 3,
    "]": 57,
    "[": 57,
    "}": 1197,
    "{": 1197,
    ">": 25137,
    "<": 25137,
}

counter = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


def get_open_always(c):
    if c in counter.keys():
        return counter[c]
    return c


def is_broken(stack, c):
    b = counter[c]  # ) -> (
    if not stack[b]:
        return True
    last_pos = stack[b][-1]
    for s, queue in stack.items():
        if s != b and queue and queue[-1] > last_pos:
            return True
    return False


def main():
    total = 0
    for x, line in enumerate(get_input()):
        stack = {
            "(": [],
            "[": [],
            "{": [],
            "<": [],
        }
        for i, c in enumerate(line):
            if c in stack:
                stack[c].append(i)
            else:
                b = counter[c]
                if is_broken(stack, c):
                    total += table[b]
                    break
                stack[b].pop()

    print(total)


if __name__ == "__main__":
    main()
