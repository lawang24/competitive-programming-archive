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
    vals = get_list_int()
    
    graph = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = get_list_int()
        u-=1
        v-=1
        graph[u].append(v)
        graph[v].append(u)
        
    queue = deque([0])
    
    ans = 0
    seen = [False for _ in range(n)]
    
    # traverse
    while queue:
        curr_node = queue.popleft()
        seen[curr_node] = True
        
        children = []
        
        for nei in graph[curr_node]:
            if not seen[nei]:
                children.append(nei)
                
        if len(children) == 1:
            if vals[children[0]] >= vals[curr_node]:
                queue.append(children[0])
                continue
            ans = children[0]
            break
        
        if children:
            # sort the children
            children.sort(key=lambda x: vals[x], reverse=True)
            # adult is greater than all
            if vals[children[0]] < vals[curr_node]:
                ans = children[0]
                break
            else:
                
                
            elif len(children) > 1:
                while 
                
        
        
        