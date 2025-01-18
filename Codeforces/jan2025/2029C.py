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

for count in range(t):
    
    n = get_int()
    n += 1
    a = [0] + get_list_int()
    dp = [[-math.inf for _ in range(3)] for _ in range(n)]
    dp[0][0] = 0

    # 0 - no skip
    # 1 - prev skipped
    # 2 - no skips left

    for i in range(1, n):
        
        # no skip case
        dp[i][0] = dp[i - 1][0]
        if a[i] > dp[i][0]:
            dp[i][0] += 1
        elif a[i] < dp[i][0]:
            dp[i][0] -= 1

        # skip case:
        # start skipping or keep skipping
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])

        # no skips left
        # stop skipping or proceed after already skipped interval
        # already skipped case
        # stop skipping
        # no skip case
        dp[i][2] = max(dp[i - 1][1], dp[i - 1][2])
        if a[i] > dp[i][2]:
            dp[i][2] += 1
        elif a[i] < dp[i][2]:
            dp[i][2] -= 1

    print(max(dp[-1][1], dp[-1][2]))