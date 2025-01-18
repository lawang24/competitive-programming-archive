import sys
from collections import deque
from collections import Counter
import math
import heapq
import functools

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


t = get_int()


def compare(a, b):
    if matrix[a - 1][b - 1] == 1:
        return a-b
    return b-a


for _ in range(t):

    n = get_int()
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in get_string()])

    ans = list(range(n, 0, -1))

    ans.sort(key=functools.cmp_to_key(compare))

    printNumArr(ans)
