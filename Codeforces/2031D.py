import sys
from collections import deque
from collections import Counter
import math
import heapq
import bisect

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
    trees = get_list_int()
    
    ans = [0 for _ in range(n)]
    _max= max(trees)
    _max_index = trees.index(_max)
    # everything after max can go directly to max
    for i in range(_max_index, n):
        ans[i] = _max
    
    prefix = [0 for _ in range(n)]
    for i in range(n):
        prefix[i] = max(prefix[i-1], trees[i])
    
    sorted_values = [(trees[i], i) for i in range(n)]
    # sort by values, and then index
    # we want the rightmost index
    sorted_values.sort(key= lambda x: (x[0], x[1]))
    
    for i in range(_max_index-1, -1, -1):
        
        # one under the current value
        right_tree_idx = bisect.bisect_left(sorted_values, trees[i], key= lambda x: x[0])
        # traversable trees
        shorter_trees = sorted_values[:right_tree_idx]
        if shorter_trees:
            # find the rightmost traversable tree
            shorter_trees.sort(key= lambda x: x[1])
            right_jump_index = shorter_trees[-1][1]
            right_jump_value = prefix[right_jump_index]
        else:
            right_jump_value = 0
        
        ans[i] = max(prefix[i], trees[i], right_jump_value)
        prefix[i] = ans[i]
        
    print(ans)