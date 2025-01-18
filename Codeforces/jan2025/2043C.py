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
    nums = get_list_int()
    
    i = 0
    while i < n:
        if abs(nums[i]) != 1:
            break
        i+=1
        
    ans = set()
    
    # outlier case
    if i != n:
        j = i
        curr = 0
        l_min = curr
        l_max = curr
        
        # go left
        for ptr in range(j-1, -1, -1):
            curr+=nums[ptr]
            l_min = min(l_min, curr)
            l_max = max(l_max, curr)
            
        # go right
        curr = 0
        r_min = curr
        r_max = curr
        j = i
        
        for ptr in range(j+1, n):
            curr+=nums[ptr]
            r_min = min(r_min, curr)
            r_max = max(r_max, curr)
        
        outlier_max = l_max + r_max + nums[i]
        outlier_min = l_min + r_min + nums[i]
        
        ans.update(set(range(outlier_min, outlier_max+1)))
    
    prefix_sum = [0 for _ in range(n)]
    _min = _max = 0
    
    for i in range(n):
        if abs(nums[i])!=1:
            continue
        prefix_sum[i] = prefix_sum[i-1] + nums[i]
        _min = min(_min, prefix_sum[i])
        
        
    ans.update(set(range(_min, _max+1)))
    
    print(len(ans))
    printNumArr(sorted(ans))    

        
