#!usr/bin/env python3.9
import itertools
from collections import defaultdict


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    points = [map(int, line.split(",")) for line in get_input() if "," in line]
    folds = [line for line in get_input() if line.startswith("fold")]
    print(folds)

    for fold in folds:
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
        points = new_points

    X = max(x for x, y in points)
    Y = max(y for x, y in points)
    for i in range(Y + 1):
        ans = ""
        for j in range(X + 1):
            ans += "X" if (j, i) in points else " "
        print(ans)


if __name__ == "__main__":
    main()
