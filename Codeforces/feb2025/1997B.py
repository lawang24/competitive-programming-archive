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
    
    grid = []
    
    for _ in range(2):
        grid.append(list(get_string()))
        
    count = 0
        
    for row in range(2):
        for col in range(1,n-1):
            if grid[row][col] == "x":
                continue
            
            other_row = 1 - row
            if grid[other_row][col] == "." and grid[row][col+1] == "." and grid[row][col-1]== "." \
                and grid[other_row][col-1] == "x" and grid[other_row][col+1] == "x":
                count += 1
    
    print(count)