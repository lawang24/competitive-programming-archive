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

MOD = 998244353

for _ in range(t):
    n = get_int()
    
    graph = [[] for _ in range(n)]
    
    p_list = get_list_int()
    for i,p in enumerate(p_list):
        graph[p-1].append(i+1)
        
    dp = [0 for _ in range(n)]
    queue = deque([0])
    old_tot = 0
    ans = 0
    while queue:
        new_tot = 0
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            
            # root
            if curr_node == 0:
                dp[curr_node] = 1
            # second layer
            elif p_list[curr_node-1] == 1:
                dp[curr_node] = 1
                new_tot += dp[curr_node]
            else:
                dp[curr_node] = old_tot - dp[p_list[curr_node-1]-1]
                new_tot += dp[curr_node]
                
            for nei in graph[curr_node]:
                queue.append(nei)
                
            ans += dp[curr_node]
            
        old_tot = new_tot 
    
    print(ans % MOD)
    
