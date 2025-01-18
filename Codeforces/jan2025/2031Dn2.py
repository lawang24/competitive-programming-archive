import sys
from collections import deque
from collections import Counter
import math
import heapq
import bisect

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
    n = get_int()
    trees = get_list_int()
    
    ans = [0 for _ in range(n)]
    max_prefix = [0 for _ in range(n)]
    max_prefix[0] = trees[0]
    for i in range(1,n):
        max_prefix[i] = max(trees[i],max_prefix[i-1])
    
    min_suffix = [0 for _ in range(n)]
    min_suffix[-1] = trees[-1]
    for i in range(n-2, -1, -1):
        min_suffix[i] = min(trees[i], min_suffix[i+1])
    
    ans[-1] = max_prefix[-1]
    
    for i in range(n-2, -1, -1):
        if max_prefix[i] > min_suffix[i+1]:
            ans[i] = ans[i+1]
        else:
            ans[i] = max_prefix[i]    
    
    printNumArr(ans)