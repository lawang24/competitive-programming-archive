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

def helper(n, k):
    if 1 << int(math.log2(n)) == n:
        return [k for _ in range(int(math.log2(n)))]

    

for _ in range(t):
    
    n, k  = get_list_int()
    array = [[k]]
    
    for i in range(2,n+1):
        new_arr = []
        for j in range(i):
            if j == 0:
                new_arr.append(array[-1][0])
            elif j == i-1:
                new_arr.append(array[-1][-1])
            else:
                new_arr.append(array[-1][j-1] ^ array[-1][j])
                
        array.append(new_arr)                
    
   
    
