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
    points = get_list_int()
    jumps = get_list_int()
    
    prefix = [0 for _ in range(n+1)]
    for i in range(n):
        prefix[i+1] = prefix[i] + points[i]
    
    graph = [None for _ in range(n)]
    graph[0] = [(jumps[0]-1, points[0])]
    for i in range(1,n):
        graph[i] = [(i-1, 0),  (jumps[i]-1, points[i])]

    # djikstras
    penalty = [math.inf for _ in range(n)]
    
    # nodes to be processed
    queue = [(0,0)]
    
    while queue:
        
        distance, curr_node = heapq.heappop(queue)
        
        # skip seen
        if penalty[curr_node] != math.inf:
            continue
        
        penalty[curr_node] = distance
        
        for nei, distance in graph[curr_node]:
            new_distance = distance + penalty[curr_node]
            if new_distance < penalty[nei]:
                heapq.heappush(queue, (new_distance, nei))
            
    champ = 0
    for i in range(n):
        champ = max(champ, prefix[i+1]- penalty[i])     
        
    print(champ)
        