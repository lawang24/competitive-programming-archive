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
    
    n , k = get_list_int()
    a = get_list_int()
    
    if n == k:
        val = 1
        idx = 1
        while idx < n and a[idx]==val:
            val+=1
            idx+=2
        print(val)
        continue
    
    flag = False
    for i in range(1,2+n-k):
        if a[i] != 1:
            flag = True
            break
    
    if flag:
        print(1)
    else:
        print(2)
            
    