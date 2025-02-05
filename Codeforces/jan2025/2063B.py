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
    n, l , r = get_list_int()
    nums = get_list_int()
    pre = sorted(nums[:l-1])
    mid = sorted(nums[l-1:r], reverse=True)
    post = sorted(nums[r:])
    
    orig = sum(mid)
    i = 0
    
    ans = orig
    
    pre_sum, mid_sum, post_sum = 0, 0, 0
    
    while i < min(max(len(pre),len(post)), len(mid)):
        
        mid_sum += mid[i]
        
        if i < len(pre):
            pre_sum += pre[i]
            ans = min(ans, orig - mid_sum + pre_sum)
            
        if i < len(post):
            post_sum += post[i]
            ans = min(ans, orig - mid_sum + post_sum)
            
        i+=1
    
    print(ans)
    
    