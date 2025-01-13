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
    current = get_list_int()
    target = get_list_int()
    
    difference = [0 for _ in range(n)]
    
    for i in range(n):
        if current[i] >= target[i]:
            continue
        
        diff = target[i] - current[i]
        
        if i-1 >= 0:
            difference[0] -= diff
            # get this one to speed
            difference[i] += diff
            
        if i+1 < n:
            # subtract last diff plus range minus
            difference[i+1] -= 2* diff
            
        difference[i]+= diff
        
    adjustment = 0
    flag = False
    for i in range(n):
        adjustment+=difference[i]
        if current[i] + adjustment < target[i]:
            print('NO')
            flag = True
            break
    
    if not flag:
        print('YES')
    
            