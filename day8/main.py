#!usr/bin/env python3.9
def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def main():
    l = {
        1: 2,
        4: 4,
        7: 3,
        8: 7,
    }
    lines = [x.split(" | ")[1] for x in get_input()]

    c = 0
    for res in lines:
        for word in res.split(" "):
            c += int(len(word) in l.values())

    print(c)


if __name__ == "__main__":
    main()
