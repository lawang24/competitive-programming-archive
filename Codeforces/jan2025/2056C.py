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
    ans = [0 for _ in range(n)]
    ans[0] = 1
    ans[1] = 1
    ans[2] = 2
    ans[-1] = 2
    ans[-2] = 1
    for i in range(3,n-2):
        ans[i] = i
    printNumArr(ans)