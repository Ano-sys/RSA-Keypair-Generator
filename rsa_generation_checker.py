import sys
from simple_rsa import generate_rsa_keypair, print_keypair

def string2int(s: str) -> int:
    out = ""
    for i in range(0, len(s)):
        out += str(ord(s[i]))
    return int(out)


def int2string(x: int) -> str:
    out = ""
    inp = str(x)
    pair = ""
    for i in range(0, len(inp)):
        pair += inp[i]
        if int(pair) > 65:
            out += chr(int(pair))
            pair = ""
    return out


if __name__ == '__main__':
    print("Disclaimer: This testing code only works on strings with valid letters no numbers!\nEspecially the int2string methode can't regenerate a string from ascii char below 66\n\n")
    if len(sys.argv) < 3:
        print("Usage: python rsa_generation_checker.py [message] [key bit length]")
        exit(-1)

    m = sys.argv[1]
    bits = int(sys.argv[2])

    public, private = generate_rsa_keypair(bits)
    print_keypair(public, True)
    print()
    print_keypair(private)
    print()

    m_int = string2int(m)

    c = pow(m_int, public[0], public[1])
    print(f"Input: '{m}'")
    print(f"Input int: {m_int}")
    print(f"Encoded: {c}")

    decoded_int = pow(c, private[0], private[1])
    print(f"Decoded int: {decoded_int}")
    decoded_message = int2string(decoded_int)
    print(f"Decoded: {decoded_message}")
