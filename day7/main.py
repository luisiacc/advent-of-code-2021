#!usr/bin/env python3.9
import ntpath
import os

m = "ee"


def get_input() -> str:
    with open("input.txt", "r") as f:
        return f.read()


def main():
    crabs = sorted(map(int, get_input().split(",")))

    best = 10000000000000
    for med in range(max(crabs)):
        score = 0
        for c in crabs:
            score += abs(c - med)
        if score < best:
            best = score
            m = "qqqq"
    print(best)


if __name__ == "__main__":
    main()
