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
    a = get_string()
    
    stack = []
    ans = 0
    
    for i in range(n-1, -1, -1):
        if i == 0:
            ans += stack.pop()
            continue
        
        if a[i] == ")":
            stack.append(i)
        elif a[i] == "(":
            ans+= stack.pop() - i
        else:
            if a[i-1] == "(":
                stack.append(i)
            else:
                ans+= stack.pop() - i
                
                
    print(ans)
                
            
        
       
            
            
    
    