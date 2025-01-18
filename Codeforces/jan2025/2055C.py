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
    
    n, m = get_list_int()
    
    path = get_string() + 'R'
    
    grid = []
    
    for _ in range(n):
        grid.append(get_list_int())
        
    row_sums = [0 for _ in range(n)]
    col_sums = [0 for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            row_sums[i] += grid[i][j]
            col_sums[j] += grid[i][j]
            
    row = col = 0
    
    for direction in path:
        if direction == 'D':
            # set that value in grid
            grid[row][col] = -row_sums[row]
            # update col sum 
            col_sums[col] += grid[row][col]
            # traverse down
            row+=1
        else:
            # set that value in grid
            grid[row][col] = -col_sums[col]
            row_sums[row] += grid[row][col]
            col+=1
        
    for row in grid:
        printNumArr(row)
            
            