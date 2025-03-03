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
    
    ans = [1,1]
    champ = 0
    
    for i in range(n):
        inv = 0
        for j in range(i+1, n):
            if a[j] < a[i]:
                inv+=1
            elif a[j] > a[i]:
                inv-=1
            if inv > champ:
                champ = inv
                ans = [i+1, j+1]
                
    printNumArr(ans)
                
        
    