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
    l, r = get_list_int()
    
    lb = format(l,'032b')
    rb = format(r,'032b')
    
    base = 0
    
    i = 0
    while i < 32:
        if lb[i]!=rb[i]:
            break
        i+=1
        if lb[i] == '1':
            base|=(1<<(31-i))
    
    base |= 1<<(31-i)
    ans = []
    
    ans.append(base)
    ans.append(base-1)
    
    for i in range(l, r+1):
        if i not in (ans[0], ans[1]):
            ans.append(i)
            break
    
    printNumArr(ans)
    
    