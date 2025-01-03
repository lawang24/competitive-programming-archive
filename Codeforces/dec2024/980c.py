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
    n = get_int()
    values = []
    
    for _ in range(n):
        values.append(get_list_int())
        
    values.sort()
    ans = [y for x in values for y in x]
    
    print(" ".join([str(y) for x in values for y in x]))
    

def check_inv(_list):
    n = len(_list)
    inv = 0
    for i in range(n):
        for j in range(i+1,n):
            if _list[i] > _list[j]:
                inv+=1
    print(inv)
    
    

