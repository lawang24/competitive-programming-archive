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
    pairs_left = get_int()
    coords = []
    # each new row scale y up
    y = 0
    x = 0
    
    count = 1
    
    while pairs_left:
        coords.append([x, y])
        x+=1
        coords.append([x, y])
        count = 2
        pairs = 1
        
        while count + pairs <= pairs_left:
            x+=1
            coords.append([x, y])
            pairs += count
            count += 1
        
        pairs_left -= pairs
        
        x+=1
        y+=1
    
    print(len(coords))
    for x, y in coords:
        print(x, y)
            
        
        
        
    
    
