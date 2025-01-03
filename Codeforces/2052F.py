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
    
def solve(n,rows):
    
    """
    
    Three scenarios:
    1. either top or bottom is open
        - check and fill the right of the open one
    
    2. neither are open
        - skip
    
    3. both are open
        - check if last was also both open 
            - makes multiple possible
    """
    
    multiple = False
    possible = True
    
    for i in range(n):
        # both open scenario
        if rows[0][i] == "." and rows[1][i] == ".":
            if i > 0 and rows[0][i-1] == "." and rows[1][i-1] == ".":
                multiple = True
        # must lay horizontal
        elif rows[0][i] == ".":
            if i < n-1 and rows[0][i+1] == ".":
                rows[0][i+1] = "#"
            else:
                possible = False
                break
        # must lay horizontal
        elif rows[1][i] == ".":
            if i < n-1 and rows[1][i+1] == ".":
                rows[1][i+1] = "#"
            else:
                possible = False
                break
    
    if not possible:
        print("None")
    elif multiple:
        print("Multiple")
    else:
        print("Unique")
        
t = get_int()

for _ in range(t):
    n = get_int()
    rows = []
    for _ in range(2):
        rows.append(list(get_string()))
    solve(n,rows)
    
    
    