import sys
import collections

FILE = 1 # if needed change it while submitting

mod = 10**9+7

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def getPostOrderTraversal(root, edges):
    stack = [(root,v) for v in edges[root]]
    post_order = stack[:]
    
    while stack:
        u, v = stack.pop()
        for child in edges[v]:
            if child!=u:
                stack.append((v,child))
                post_order.append((v,child))
                
    for u, v in reversed(post_order):
        yield u, v

def getNumDivisions():
    no_child_ally_combinations = [1 for _ in range(nodes+1)]
    parent_ally_combinations = [1 for _ in range(nodes+1)]
    root = 1
    
    # u = parent, v = child
    for u, v in getPostOrderTraversal(root,edges):
        diff_child_combinations = parent_ally_combinations[v] - no_child_ally_combinations[v]
        parent_ally_combinations[u] *= (parent_ally_combinations[v]+diff_child_combinations)
        no_child_ally_combinations[u] *=  diff_child_combinations
        parent_ally_combinations[u] %= mod
        no_child_ally_combinations[u] %= mod
        
    # root is essentially a "different child" because it has no parent node to be an ally
    root_combinations = parent_ally_combinations[root] - no_child_ally_combinations[root]
    
    # x2 for symmetry of root node with other color
    return 2*(root_combinations) % mod

final_result = []
nodes = get_int()
edges = collections.defaultdict(list)

# process input edges
for _ in range(nodes-1):
    a,b = get_list_int()
    edges[a].append(b)
    edges[b].append(a)
    
ans = getNumDivisions()
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

