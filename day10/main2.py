#!usr/bin/env python3.9
import itertools


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


table = {
    ")": 1,
    "(": 1,
    "]": 2,
    "[": 2,
    "}": 3,
    "{": 3,
    ">": 4,
    "<": 4,
}

counter = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}


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
    sols = []
    for x, line in enumerate(get_input()):
        stack = {
            "(": [],
            "[": [],
            "{": [],
            "<": [],
        }
        broken = False
        for i, c in enumerate(line):
            if c in stack:
                stack[c].append(i)
            else:
                b = counter[c]
                if is_broken(stack, c):
                    broken = True
                    break
                stack[b].pop()

        if broken:
            continue

        to_fill = []
        while any(stack.values()):
            m = -1  # max
            c = None
            for s, queue in stack.items():
                if not queue:
                    continue
                local_m = max(queue)
                if local_m > m:
                    m = local_m
                    c = s

            to_fill.append(c)
            stack[c].pop()

        total = 0
        for c in to_fill:
            total *= 5
            total += table[c]
        sols.append(total)

    print(sorted(sols))
    print(sorted(sols)[len(sols) // 2])


if __name__ == "__main__":
    main()
