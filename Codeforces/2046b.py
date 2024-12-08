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

t = get_int()

for _ in range(t):
    final_values = []

    n = get_int()
    nums = get_list_int()
    purge_threshold = math.inf
    stack = []
    for curr in nums:
        
        # purged!
        if curr > purge_threshold:
            final_values.append(curr+1)
            continue
        
        while stack and curr < stack[-1]:
            removed_char = stack.pop() + 1
            final_values.append(removed_char)
            purge_threshold = min(purge_threshold, removed_char)
        stack.append(curr)
                
    final_values.sort()
    stack.extend(final_values)

    print(" ".join([str(x) for x in stack]))

        