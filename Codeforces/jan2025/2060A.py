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
    nums = get_list_int()
    champ = 0
    
    for j in range(-100, 101):
        array = nums[:2] + [j] + nums[2:]
        count = 0
        for i in range(2,5):
            if array[i] == array[i-1] + array[i-2]:
                count+=1
                
        champ = max(champ, count)
        
    print(champ)
    
    
    
    