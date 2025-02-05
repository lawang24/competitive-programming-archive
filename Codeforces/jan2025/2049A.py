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
    
    a = [0] +  get_list_int()
    
    count = 0
    # count number of subarrays of non-zeros
    
    for i in range(1,n+1):
        if a[i] != 0 and a[i-1] == 0:
            count+=1
            if count == 2:
                break
    
    print(count)
  
    