import sys
import math


def adv_euclid(m: int, n: int) -> (int, int):
    if n % m == 0:
        return 1, 0
    else:
        x_, y_ = adv_euclid(n % m, m)
        x = y_ - (n // m) * x_
        y = x_
        return x, y


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python adv_euklid.py x y")
        exit(-1)

    m = int(sys.argv[1])
    n = int(sys.argv[2])
    x, y = adv_euclid(m, n)
    ggt = m * x + n * y

    print(f"ggT: {ggt}\nx: {x}\ny: {y}")
