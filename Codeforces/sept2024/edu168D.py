import sys
import math
sys.setrecursionlimit(20005)
 
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
 
def solve(graph, values):
    
    def helper(node):
        # no children
        if not graph[node]:
            return values[node]
        _min = math.inf
        for child in graph[node]:
            _min = min(_min, helper(child))
        if values[node] > _min:
            return _min
        return (_min+values[node])//2
            
    if not graph[0]:
        return values[0]
    
    return values[0] + min(helper(child) for child in graph[0])
        
            
final_result = []
 
t = get_int()
 
for _ in range(t):
    n = get_int()
    values = get_list_int()
    graph = [[] for _ in range(n)]
    for i, v in enumerate(get_list_int()):
        graph[v-1].append(i+1)
    final_result.append(str(solve(graph, values)))
    
 
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')
 