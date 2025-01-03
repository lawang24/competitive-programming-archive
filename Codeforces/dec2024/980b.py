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
    cans = get_list_int()
    cans.sort()
    
    curr = 0
        
    for i in range(n):
        if i==0:
            curr = n*cans[i]
        else:
            curr+= (n-i) * (cans[i]-cans[i-1])
        if curr >=k:
            break
            
    print(k+i)
    