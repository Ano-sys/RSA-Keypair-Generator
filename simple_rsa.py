import sys
import sympy
import random
from check_prim import fermat_fast
from euclid import euclid
from adv_euclid import adv_euclid

def generate_prime(bits):
    return sympy.randprime(2**(bits-1), 2**bits)

def generate_rsa_primes(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)

    while p == q:
        q = generate_prime(bits)

    return p, q


def get_k(phi: int, max: int) -> int:
    for i in range(max, 2, -1):
        if fermat_fast(i) == True and euclid(i, phi) == 1 and i != phi - 1:
            return i
    return -1


def gen_rsa_keypair(p: int, q: int) -> ((int, int), (int, int)):
    n = p * q
    phi = (p - 1) * (q - 1)
    k = get_k(phi, phi - 1)
    if k == -1:
        print("Could not get a suiting k element...")
        exit(-1)

    l, _ = adv_euclid(k, phi)

    if l <= 0:
        l += phi

    return (k, n), (l, n)


def print_keypair(pair: (int, int), isPublic = False):
    if(isPublic):
        print(f"[Public Key]\nk: {pair[0]}\nn: {pair[1]}\n")
    else:
        print(f"[Private Key]\nl: {pair[0]}\nn: {pair[1]}")


def generate_rsa_keypair(bits) -> ((int, int), (int, int)):
    p, q = generate_rsa_primes(bits)
    public, private = gen_rsa_keypair(p, q)
    return public, private


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python simple_rsa.py [keylength in bits]")
        exit(-1)
    bits = int(sys.argv[1])
    p, q = generate_rsa_primes(bits)
    public, private = gen_rsa_keypair(p, q)
    print_keypair(public, True)
    print_keypair(private)
    