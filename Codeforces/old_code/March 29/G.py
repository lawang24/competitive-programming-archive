import sys
import collections
from os import path

FILE = 0

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def helper(visited, node, neighbors):
    max_count = 0
    
    for nei in neighbors[node]:
        if nei not in visited:
            visited.add(nei)
            max_count = max(max_count, helper(visited, nei, neighbors))
            visited.remove(nei)
    
    return max_count + 1
            

def find_longest_path(neighbors, node):
    
    visited = {node}
    nodes_in_longest_path = helper(visited,node,neighbors)
    
    return nodes_in_longest_path

def solve(nodes, n_nodes):
    g_group = collections.defaultdict(list)
    w_group = collections.defaultdict(list)
    neighbors = collections.defaultdict(list)
    visited = set()
    
    # declare adjacency list
    for i, node in enumerate(nodes):
        g, w = node.split()
        
        # attach to all neighbors in the same category
        for nei in g_group[g]:
            neighbors[i].append(nei)
            neighbors[nei].append(i)
        
        g_group[g].append(i)
        
        # duplicate name
        for nei in w_group[w]:
            if i not in neighbors[nei]:
                neighbors[i].append(nei)
                neighbors[nei].append(i)
            
            # add yourself to the category
        w_group[w].append(i)
    
    # find the longest path
    ans = n_nodes
    
    for i in range(n_nodes):
        if i not in visited:
            visited.add(i)
            longest_path = find_longest_path(neighbors,i)
            ans = min(ans, n_nodes-longest_path)
    
    return ans
    
n = get_int()

final_result = []

for _ in range(n):
    n_nodes = get_int()
    nodes = []
    for _ in range(n_nodes):
        nodes.append(get_string())
    ans = solve(nodes, n_nodes)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

