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
    nums = get_list_int()

    champ = 0
    if n % 2 == 0:
        for i in range(0, n, 2):
            champ = max(champ, nums[i + 1] - nums[i])
    else:
        champ = math.inf
        prefix = [0 for _ in range(n)]
        suffix = [0 for _ in range(n)]

        # store at index i the min pair distance to the left or right
        # only odd values can be removed, so we only store for odd values
        # removing an even value would pair nums[i-1] and nums[i+1]
        # which is strictly worse than the original pair using i
        for i in range(2, n, 2):
            prefix[i] = max(prefix[i - 2], nums[i - 1] - nums[i - 2])
        for i in range(n - 3, -1, -2):
            suffix[i] = max(suffix[i + 2], nums[i + 2] - nums[i + 1])

        for skipped_idx in range(0, n, 2):
            ans = 1
            ans = max(ans, suffix[skipped_idx], prefix[skipped_idx])
            champ = min(champ, ans)

    print(champ)
