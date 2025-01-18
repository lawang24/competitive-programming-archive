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
    
# use tortoise and hare on each one

t = get_int()

for _ in range(t):
    n = get_int()
    a = get_list_int()
    
    n+=1
    a = [0] + a
    
    indegrees = [0 for _ in range(n)]
    for parent, child in enumerate(a):
        indegrees[child]+=1
        
    queue = deque()
    
    for i in range(n):
        if indegrees[i] == 0:
            queue.append(i)
            
    distances = [0 for _ in range(n)]
    
    
    if not queue:
        print(2)
    else:
        ans = 0
        while queue:
            # only count leaf nodes
            curr_node = queue.popleft()
            ans = max(ans, distances[curr_node])
            
            child_node = a[curr_node]
            distances[child_node] += distances[curr_node]+1
            indegrees[child_node]-=1
            if indegrees[child_node] == 0:
                queue.append(child_node)
            
        print(ans+3)