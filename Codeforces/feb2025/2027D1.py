import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))
    
t = get_int()

for _ in range(t):
    
    n, m = get_list_int()
    a = get_list_int()
    b = get_list_int()
    
    # prefix sum for a
    prefix_sum = [0 for _ in range(n+1)]
    for i in range(n):
        prefix_sum[i+1] = prefix_sum[i] + a[i]
    
    # represents the index of the prefix_sum that goes over
    # valid prefix_sum would be from start -> r_index - 1
    # values should be between 1 -> n
    
    dp = [math.inf for _ in range(n+1)]
    dp[0] = 0
    
    for b_idx in range(m):
        right = 0
        for a_idx in range(n):
            while right < n+1 and prefix_sum[right] - prefix_sum[a_idx] <= b[b_idx]:
                right += 1
            # future values will smaller regardless
            dp[right-1] = min(dp[right-1], dp[a_idx] + m - (b_idx+1))
    
    if dp[-1] == math.inf:
        print(-1)
    else:
        print(dp[-1])