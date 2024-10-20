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

def solve(len, x, nums):
    nums.sort()
    reserve = Counter()

    curr_idx = 0
    
    for n in nums:
        # found the number we want
        if n == curr_idx:
            curr_idx+=1
        # duplicate numbers, save for later
        elif n < curr_idx:
            reserve[n%x]+=1
        else:
            # catch the numbers in between up
            while curr_idx < n:
                if reserve[curr_idx%x]:
                    reserve[curr_idx%x]-=1
                    curr_idx+=1
                else: break
            if curr_idx == n:
                curr_idx+=1
            else:
                print(curr_idx)
                return
        
    while curr_idx < len:
        if reserve[curr_idx%x]:
            reserve[curr_idx%x]-=1
            curr_idx+=1
        else: break
    
    print(curr_idx)
    return
        

t = get_int()


for _ in range(t):
    a, x = get_list_int()
    nums = get_list_int()
    solve(a, x, nums)
    


    
    