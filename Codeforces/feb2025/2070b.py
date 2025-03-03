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
    
    n, x , k = get_list_int()
    x*=-1
    commands = get_string()
    
    time_to_reset = math.inf
    time_to_zero = math.inf
    distance = 0
    
    for i in range(n):
        if commands[i] == "L":
            distance -=1
        else:
            distance +=1
        
        if distance == x:
            time_to_reset = i+1
            break
        
    
    if time_to_reset == math.inf or time_to_reset > k:
        print(0)
        continue
        
    k-=time_to_reset
    
    time_to_zero = math.inf
    distance = 0
    
    for i in range(n):
        if commands[i] == "L":
            distance -=1
        else:
            distance +=1
        
        if distance == 0:
            time_to_zero = i+1
            break
            
    values = 1
    
    if time_to_zero != math.inf:
       values+= k//time_to_zero
    
    print(values)
        
    