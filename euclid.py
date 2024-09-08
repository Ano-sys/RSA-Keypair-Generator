import sys

def euclid(m: int, n: int):
    if n % m == 0:
        return m
    else:
        return euclid(n % m, m)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python euklid.py x y")
        exit(-1)

    print(f"ggT: {euclid(int(sys.argv[1]), int(sys.argv[2]))}")
    
