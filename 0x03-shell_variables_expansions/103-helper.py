#!/usr/bin/env python3
import sys

def to_int(s, alphabet):
    idx = {c: i for i, c in enumerate(alphabet)}
    base = len(alphabet)
    v = 0
    for ch in s:
        if ch not in idx:
            continue
        v = v * base + idx[ch]
    return v

def to_base(n, alphabet):
    if n == 0:
        return alphabet[0]
    base = len(alphabet)
    digits = []
    while n > 0:
        digits.append(alphabet[n % base])
        n //= base
    return ''.join(reversed(digits))

if __name__ == "__main__":
    # read WATER and STIR from stdin (space-separated)
    data = sys.stdin.read().strip().split()
    water_s, stir_s = data if len(data) == 2 else ("", "")

    alph_water = list("water")
    alph_stir = list("stir")
    alph_best = list("bestchol")

    n1 = to_int(water_s, alph_water)
    n2 = to_int(stir_s, alph_stir)
    total = n1 + n2
    print(to_base(total, alph_best))
