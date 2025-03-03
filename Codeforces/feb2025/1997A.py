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
    pw = get_string()
    if pw[-1] == 'a':
        ans = pw + "b"
    else:
        ans = pw + "a"
        
    
    flag = False
    
    for i in range(1,len(pw)):
        if pw[i] == pw[i-1]:
            if pw[i] == "a":
                ans = pw[:i] + "b" + pw[i:]
            else:
                ans = pw[:i] + "a" + pw[i:]

    print(ans)