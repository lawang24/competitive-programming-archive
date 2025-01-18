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
    
    possible = False
    
    n = get_int()
    nums = get_list_int()
    
    for i in range(1,n):
        a, b = nums[i-1], nums[i]
        
        if a>b:
            a, b = b, a
        
        if a > b/2:
            possible = True
            break
        
    if possible:
        print('YES')
    else:
        print('NO')
        
    