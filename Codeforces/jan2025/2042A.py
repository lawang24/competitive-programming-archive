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
    chests = get_list_int()
    chests.sort(reverse=True)
    
    count = 0
    
    for i in range(n):
        if count+chests[i] > k:
            break
        count+=chests[i]
    
    print(k-count)