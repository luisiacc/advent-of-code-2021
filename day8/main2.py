#!usr/bin/env python3.9
import itertools


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


def i(letter):
    return "abcdefg".index(letter)


def _sort(word):
    return "".join(sorted(word))


def main():
    X = [x.split(" | ") for x in get_input()]

    combs = {}
    for p in itertools.permutations("abcdefg"):
        q = [
            p[i("a")] + p[i("b")] + p[i("c")] + p[i("e")] + p[i("f")] + p[i("g")],  # 0
            p[i("c")] + p[i("f")],  # 1
            p[i("a")] + p[i("c")] + p[i("d")] + p[i("e")] + p[i("g")],  # 2
            p[i("a")] + p[i("c")] + p[i("d")] + p[i("f")] + p[i("g")],  # 3
            p[i("b")] + p[i("c")] + p[i("d")] + p[i("f")],  # 4
            p[i("a")] + p[i("b")] + p[i("d")] + p[i("f")] + p[i("g")],  # 5
            p[i("a")] + p[i("b")] + p[i("d")] + p[i("e")] + p[i("f")] + p[i("g")],  # 6
            p[i("a")] + p[i("c")] + p[i("f")],  # 7
            p[i("a")] + p[i("b")] + p[i("c")] + p[i("d")] + p[i("e")] + p[i("f")] + p[i("g")],  # 8
            p[i("a")] + p[i("b")] + p[i("c")] + p[i("d")] + p[i("f")] + p[i("g")],  # 9
        ]
        q = [_sort(w) for w in q]
        combs["".join(p)] = q

    c = 0
    for digits, output in X:
        digits = [_sort(x) for x in digits.split()]
        output = [_sort(x) for x in output.split()]
        for comb in combs.values():
            if set(digits) == set(comb):
                n = ""
                for d in output:
                    n += str(comb.index(d))
                c += int(n)
                break
    print(c)


if __name__ == "__main__":
    main()
