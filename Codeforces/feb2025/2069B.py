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
    
DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    
t = get_int()

for _ in range(t):
    
    n, m = get_list_int()
    
    arr = []
    
    for _ in range(n):
        arr.append(get_list_int())
    
    per_color_count = [0 for _ in range(n*m+1)]
    adjacent = False
    
    for row in range(n):
        for col in range(m):
            per_color_count[arr[row][col]] = max(1,per_color_count[arr[row][col]])
            for dx, dy in DIR:
                nx, ny = row + dx, col + dy
                if 0<=nx<n and 0<=ny<m and arr[nx][ny] == arr[row][col]:
                    per_color_count[arr[row][col]] = 2
                    adjacent = True
                    
    if adjacent:
        print(sum(per_color_count)-2)
    else:
        print(sum(per_color_count)-1)
                
    
    
        
    
    