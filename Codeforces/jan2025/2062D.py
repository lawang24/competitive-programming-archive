import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    return int(sys.stdin.readline())


def get_string():
    return sys.stdin.readline().strip()


def get_list_int():
    return list(map(int, get_string().split()))


def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))


t = get_int()

for _ in range(t):

    n = get_int()
    adj = [[] for _ in range(n)]
    vals = [0 for _ in range(n)]
    degrees = [0 for _ in range(n)]
    bounds = [[] for _ in range(n)]

    # get initial vals
    for i in range(n):
        l, r = get_list_int()
        bounds[i] = [l,r]
        vals[i] = l

    # create graph
    for _ in range(n - 1):
        u, v = get_list_int()
        u, v = u-1, v-1
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
        
    queue = deque()
        
    for i in range(n):
        # get leaves
        if degrees[i] == 1:
            queue.append(i)
            
    addition = 0
    
    # in case only one node
    curr_node = 0
    
    while queue:
        curr_node = queue.popleft()
        
        # set to seen
        degrees[curr_node] -= 1
        
        for nei in adj[curr_node]:
            # seen already, there should only be one valid neighbor
            if degrees[nei] == 0:
                continue
            
            # root is lower value
            if vals[nei] < vals[curr_node]:
                vals[nei] = min(vals[curr_node], bounds[nei][1])
                addition += vals[curr_node] - vals[nei]
                
            degrees[nei]-=1
            if degrees[nei] == 1:
                queue.append(nei)
            
    print(addition + vals[curr_node])
                
                