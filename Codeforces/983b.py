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
    n, k = get_list_int()
    
    if n == 1:
        print(1)
        print(1)
    elif k == 1 or k == n:
        print(-1)
    else:
        # even median means sides are odd
        if k % 2 == 0:
            ans = [1, k, k+1]
        # odd median
        else:
            ans = [1,2,k,k+1,n]
        print(len(ans))
        print(" ".join([str(x) for x in ans]))
    
    
    
