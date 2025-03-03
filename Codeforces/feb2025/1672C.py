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
    pairs = []
    
    for i in range(n-1):
        if a[i] == a[i+1]:
            pairs.append(i)
    
    if len(pairs) <= 1:
        print('0')
    else:
        print(max(1,pairs[-1] - pairs[0] - 1))