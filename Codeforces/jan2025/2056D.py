import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    return int(sys.stdin.readline())


def get_string():
    return sys.stdin.readline().strip()


def get_list_int():
    return list(map(int, get_string().split()))


def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))


t = get_int()

for _ in range(t):
    n = get_int()
    nums = get_list_int()
    ans = 0

    for median in range(1, 11):

        count = Counter()
        curr_sum = 0
        last_x = 0
        
        prefix = [0 for _ in range(n+1)]
        
        for i in range(1,n+1):
            
            pseudo = 1 if nums[i-1] > median else -1
            prefix[i] = prefix[i-1] + pseudo
            
            if nums[i-1] == median:
                while last_x < i:
                    count[prefix[last_x]]+=1
                    last_x+=1
                
            ans+=count[prefix[i]]
        
    
    print(n*(n+1)//2 - ans)             
            
            