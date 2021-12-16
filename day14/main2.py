#!usr/bin/env python3.9
import itertools
from collections import Counter, defaultdict


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


template = get_input()[0]
codes = [x.split(" -> ") for x in get_input()[2:]]


def match(pair):
    return next(x[1] for x in codes if x[0] == pair)


def main():
    c = defaultdict(int)
    for i in range(len(template)):
        if i + 1 < len(template):
            c[template[i] + template[i + 1]] += 1

    for i in range(40):
        new_c = defaultdict(int)
        for pair in c:
            m = match(pair)
            a, b = list(pair)
            new_c[a + m] += c[pair]
            new_c[m + b] += c[pair]
        c = new_c

    b = defaultdict(int)
    for pair, count in c.items():
        b[pair[0]] += count
        b[pair[1]] += count

    for letter in b:
        b[letter] = (b[letter] + 1) // 2

    bigger = max(b, key=lambda x: b[x])
    lower = min(b, key=lambda x: b[x])
    print(b[bigger] - b[lower])


if __name__ == "__main__":
    main()
