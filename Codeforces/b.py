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

def solve(n1, n2):
    mod = 10**9 + 7
    ans = pow(2,n2,mod)
    print(ans)
    
t = get_int()

for _ in range(t):
    l1 = get_list_int()
    l2 = get_list_int()
    
    for i in range(len(l1)):
        solve(l1[i], l2[i])