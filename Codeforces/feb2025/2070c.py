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

def solve(mid):
    last = ''
    count = 0
    
    for i in range(n):
        if penalties[i] > mid:
            if last != 'B' and colors[i] == 'B':
                count+=1
            last = colors[i]
    
    return count <= k


for _ in range(t):
    n, k = get_list_int()
    colors = get_string()
    penalties = get_list_int()
    
    lo, hi = 0, max(penalties)
    
    while lo < hi:
        
        mid = (lo+hi) // 2
        
        if solve(mid):
            hi = mid
        else:
            lo = mid + 1
            
    print(hi)
            