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

t = get_int()

for i in range(t):
    n = get_int()
    columns = get_list_int()
   
    swaps = []

   
    
    one_pointer = 0
    while one_pointer<n and columns[one_pointer]!=1:
        one_pointer+=1
    
    two_pointer = 0
    hi = n-1
    while two_pointer<hi:
        
        # find the lowest 2
        while two_pointer<hi and columns[two_pointer]!=2:
            two_pointer+=1
        
        # find a right 0 or 1
        while two_pointer<hi and columns[hi]==2:
            hi-=1
        
        if not two_pointer<hi:
            break
        
        # hi = 1
        if columns[hi] == 1:
            columns[hi], columns[two_pointer] = columns[two_pointer], columns[hi]
            swaps.append((hi,two_pointer))
            one_pointer = two_pointer
            two_pointer+=1
        # hi = 0
        else:
            columns[one_pointer] = 0
            columns[hi] = 2
            columns[two_pointer] = 1
            swaps.append((one_pointer,hi))
            swaps.append((two_pointer,hi))
            one_pointer = two_pointer
    
    lo , hi = 0, n-1
    
    while lo < hi:
        
        # get to a 1
        while lo < hi and columns[lo] != 1:
            lo+=1
            
        # get to a 0
        while lo < hi and columns[hi] != 0:
            hi-=1
        columns[lo], columns[hi] = columns[hi], columns[lo]
        
        if lo<hi:
            swaps.append((lo, hi))    
    
    print(len(swaps))
    for key in swaps:
        print(key[0]+1, key[1]+1)