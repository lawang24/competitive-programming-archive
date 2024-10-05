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

def calcSpots(i, j, n, m, k ):
    r1 = max(0, i-k+1)
    r2 = min(n-1, i+k-1)
    height = r2 - r1 + 2 - k
    # print(r2, r1, i, j, k)
    # print('height',height)
    r1 = max(0, j-k+1)
    r2 = min(m-1, j+k-1)
    width = r2 - r1 - k + 2
    # print(height, width)
    return width * height
    x

def solve(n, m, k, heights):
    heights.sort(reverse = True)
    spots = []
    for i in range(n):
        for j in range(m):
            spots.append(calcSpots(i, j, n, m , k))
            
    spots.sort(reverse=True)
    
    ans = 0
    
    for i, v in enumerate(heights):
        ans+= spots[i] * v
            
    return ans
            


final_result = []

t = get_int()

for _ in range(t):
    n, m, k = get_list_int()
    w = get_int()
    heights = get_list_int()
    ans = solve(n, m, k, heights)
    final_result.append(str(ans))
    
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

