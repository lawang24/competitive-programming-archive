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
    n, k = get_list_int()
    
    fish = get_string()
    
    diff = 0
    suffixes = []
    for i in range(n-1, 0, -1):
        c = fish[i]
        if c == "1":
            diff+=1
        else:
            diff-=1
        if diff > 0:
            suffixes.append(diff)
    
    suffixes.sort(reverse=True)
    
    points = 0
    i = 0
    while i < len(suffixes):
        if points >= k:
            break
        points += suffixes[i]
        i+=1
        
       
    if points < k:
        print(-1)
    else:
        print(i+1)
        
    
    