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

t = get_int()

for _ in range(t):
    n , k = get_list_int()
    s = get_string()
    t = get_string()
    
    done = False
    lo = max(0, n-k)
    hi = min(k, n)
    
    # check ones that have to match
    for i in range(lo, hi):
        if s[i] != t[i]:
            print("NO")
            done = True
            break
    
    if not done:
        if sorted(s) == sorted(t):
            print('YES')
        else:
            print('NO')
    