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

t = get_int()

for _ in range(t):
    n = get_int()
    a = get_list_int()
    a.sort()
    pairs = []
    for i in range(n-1):
        pairs.append(a[i]+a[i+1])
        
    champ = math.inf
    
    # binary search through 
    for i in range(n):
        left_movements = bisect.bisect_right(pairs, a[-1-i])
        ans = i+left_movements
        champ = min(champ, ans)
        
    print(champ)