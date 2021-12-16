#!usr/bin/env python3.9
import itertools
from collections import Counter, defaultdict


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


template = get_input()[0]
codes = [x.split(" -> ") for x in get_input()[2:]]


def match(l1, l2):
    return next(x[1] for x in codes if x[0] == l1 + l2)


def merge(w1, w2):
    new_word = ""
    for i in range(len(w1)):
        new_word += w1[i]
        if i < len(w2):
            new_word += w2[i]
    return new_word


def main():
    new_template = template
    for i in range(40):
        result = ""
        for i, w in enumerate(new_template):
            if i < len(new_template) - 1:
                result += match(w, new_template[i + 1])
        new_template = merge(new_template, result)

    counter = Counter(list(new_template))
    bigger = max(counter, key=lambda x: counter[x])
    lower = min(counter, key=lambda x: counter[x])
    print(counter[bigger] - counter[lower])


if __name__ == "__main__":
    main()
