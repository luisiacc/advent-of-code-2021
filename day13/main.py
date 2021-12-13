#!usr/bin/env python3.9
import itertools
from collections import defaultdict


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    points = [map(int, line.split(",")) for line in get_input() if "," in line]
    fold = [line for line in get_input() if line.startswith("fold")][0]

    c = 0
    d, pos = fold.strip("fold along ").split("=")
    pos = int(pos)

    new_points = set()
    for x, y in points:
        if d == "y" and y > pos:
            new_points.add((x, 2 * pos - y))
        elif d == "x" and x > pos:
            new_points.add((2 * pos - x, y))
        else:
            new_points.add((x, y))

    print(len(new_points))


if __name__ == "__main__":
    main()
