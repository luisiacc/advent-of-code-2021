#!/usr/bin/env python3.9

def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    lines = get_input()

    pos = 0
    depth = 0
    for line in lines:
        command, n = line.split(" ")
        n = int(n)
        if command == "forward":
            pos += n
        if command == "down":
            depth -= n
        if command == "up":
            depth += n

    print(abs(pos * depth))


if __name__ == "__main__":
    main()
