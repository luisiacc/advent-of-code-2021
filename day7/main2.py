#!usr/bin/env python3.9
def get_input() -> str:
    with open("input.txt", "r") as f:
        return f.read()


def main():
    crabs = sorted(map(int, get_input().split(",")))

    best = 10000000000000
    for med in range(max(crabs)):
        score = 0
        for c in crabs:
            n = abs(c - med)
            score += n * (n + 1) // 2
        if score < best:
            best = score
    print(best)


if __name__ == "__main__":
    main()
