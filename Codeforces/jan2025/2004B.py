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
    a, b = get_list_int()
    c, d  = get_list_int()
    
    l = max(a,c)
    r = min(b,d)
    
    if l > r:
        print(1)
        continue
    
    ans = r-l+2
    if a == c:
        ans-=1
    if b == d:
        ans-=1
    print(ans)
    
    