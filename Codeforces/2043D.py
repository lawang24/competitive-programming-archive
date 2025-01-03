import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    return int(sys.stdin.readline())


def get_string():
    return sys.stdin.readline().strip()


def get_list_int():
    return list(map(int, get_string().split()))


def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))


def solve(l, r, g):

    if l % g != 0:
        l += g - (l % g)
    r -= r % g

    gap = r - l

    lo, hi = l, r

    while gap >= 0:
        lo = l
        hi = lo + gap
        while hi <= r:
            if math.gcd(lo, hi) == g:
                return [lo, hi]
            lo += g
            hi += g
        gap -= g

    return [-1, -1]


t = get_int()

for _ in range(t):
    l, r, g = get_list_int()

    printNumArr(solve(l, r, g))
