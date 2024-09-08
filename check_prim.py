import sys

def fermat_save(x: int) -> bool:
    # print("[Save Check]")
    if x <= 1:
        return False
    for a in range(2, x):
        if pow(a, x-1, x) != 1:
            return False
    return True

def fermat_fast(x: int) -> bool:
    # print("[Fast Check]")
    if x <= 1:
        return False
    if pow(2, x-1, x) != 1:
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python check_prim.py x")
        exit(-1)
    if len(sys.argv) == 3 and sys.argv[2] == 'fast':
        operation = fermat_fast
    else:
        operation = fermat_save

    x = int(sys.argv[1])
    m = '' if operation(x) else 'not '
    print(f"{x} is {m}a prime number!")
