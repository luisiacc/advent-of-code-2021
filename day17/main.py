import itertools
from collections import Counter, defaultdict, deque


def get_input():
    with open("input.txt", "r") as f:
        return [x.strip() for x in f.readlines()]


# test target area: x=20..30, y=-10..-5
# real target area: x=56..76, y=-162..-134


def main():
    # area_x = (20, 30)
    # area_y = (-10, -5)

    area_x = (56, 76)
    area_y = (-162, -134)

    higher = 0
    for VX in range(0, 1000):
        for VY in range(-500, 500):
            m = 0
            vx = VX
            vy = VY
            x, y = 0, 0
            while 1:
                if x > area_x[1] or y < area_y[0]:
                    break
                if area_x[0] <= x <= area_x[1] and area_y[0] <= y <= area_y[1]:
                    higher = max(m, higher)
                    break
                x += vx
                y += vy
                m = max(m, y)
                vy -= 1
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1

    print(higher)


if __name__ == "__main__":
    main()
