import sys
import collections
import math
import heapq

sys.setrecursionlimit(2*(10**5))

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
    
def test(edges):
    
    test_ans = 0
    G = edges
    
    def dfs(u, p):
        nonlocal test_ans
        child_highest_degree = float('-inf')
        child_second_degree = float('-inf')
        
        for v in G[u]:
            if v != p:
                
                # direct connection, 2nd degree connection
                q_first, q_second = dfs(v, u)
                
                # direct connection with child
                test_ans = max(test_ans, len(G[u]) + q_first - 2)
                
                # connection with grandchildren
                test_ans = max(test_ans, len(G[u]) + q_second - 1)
                
                # go through the root
                # store the top two children
                curr_branch_max = max(q_first, q_second)
                if curr_branch_max > child_highest_degree:
                    child_second_degree = child_highest_degree
                    child_highest_degree = curr_branch_max
                elif curr_branch_max > child_second_degree:
                    child_second_degree = curr_branch_max
                    
                test_ans = max(test_ans, child_highest_degree + child_second_degree - 1)
                
                    
        # returns the degrees + max of prev node (lower in tree)
        return (len(G[u]), child_highest_degree)

    dfs(0, -1)
    
    return test_ans
    
t = get_int()

for _ in range(t):
    
    n = get_int()
    adj = [[] for _ in range(n)]
    
    for i in range(n-1):
        u, v = get_list_int()
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
        
    ans = test(adj)
    
    print(ans)
        
                    
    