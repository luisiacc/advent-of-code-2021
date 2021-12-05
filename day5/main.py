#!/usr/bin/env python3.9
from collections import namedtuple

def get_input() -> list[str]:
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


Vector = namedtuple("Vector", ["x1", "y1", "x2", "y2"])

def main():
    vectors = get_input()
    vectors = [Vector(*map(int, v.replace(" -> ", ",").split(","))) for v in vectors]
    vectors = [v for v in vectors if v.x1 == v.x2 or v.y1 == v.y2]

    matrix = {}

    for vector in vectors:
        x1, x2 = min(vector.x1, vector.x2), max(vector.x1, vector.x2)
        y1, y2 = min(vector.y1, vector.y2), max(vector.y1, vector.y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) not in matrix:
                    matrix[(x, y)] = 0
                matrix[(x, y)] += 1

    count = 0
    for pair in matrix:
        if matrix[pair] > 1:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
