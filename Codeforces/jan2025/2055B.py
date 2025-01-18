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
    
    i = 0 
    
    while i < n:
        if current[i] < target[i]:
            diff = target[i]-current[i]
            break
        i+=1
    
    if i == n:
        print('YES')
        continue
    
    flag = True
    
    for j in range(n):
        if i == j:
            continue
        
        excess = current[j] - target[j]
        if excess < 0 or excess < diff:
            print('NO')
            flag = False
            break
        
    if flag:
        print("YES")
    
            
        
        
            