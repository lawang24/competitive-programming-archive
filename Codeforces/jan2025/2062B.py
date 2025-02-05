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
    
    n = get_int()
    a = get_list_int()
    
    flag = True
    
    for i in range(n):
        v = a[i]
        side = max(i*2,(n-i-1) * 2)
        if v <= side:
            flag = False
            break
        
    
    if flag:
        print('YES')
    else:
        print('NO')