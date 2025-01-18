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


t = get_int()

for _ in range(t):
    n = get_int()
    pairs = []
    ans = [0 for _ in range(n)]
    original = []

    for i in range(n):
        l, r = get_list_int()
        original.append((l,r))
        pairs.append((l, r, i))

    pairs.sort(key=lambda x: (x[0], -x[1]))

    # maintain a decreasing order right bound
    # because otherwise all other options are invalid
    stack = []

    for l, r, i in pairs:
        while stack and stack[-1][1] < r:
            stack.pop()
        # we take the left side of this
        if stack:
            ans[i] += l - stack[-1][0]
        stack.append((l, r))
    
    pairs.sort(key=lambda x: (-x[1], x[0]))
    
    stack = []
    
    for l, r, i in pairs:
        while stack and l < stack[-1][0] :
            stack.pop()
        # we take the right side
        if stack:
            ans[i] += stack[-1][1] - r
        stack.append((l, r))
        
    for i in range(n-1):
        l1, r1, idx = pairs[i]
        l2, r2 ,idx2 = pairs[i+1]
        if l1 == l2 and r1 == r2:
            ans[idx] = ans[idx2] = 0
        
    for val in ans:
        print(val)
