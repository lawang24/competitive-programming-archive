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

def solve(n, a):
    
    for i in range(n):
        if a[i] % 2 != a[0] % 2:
            print('-1')
            return
    
    answer = []
    print('31')
    answer.append(str(a[0]%2+1))
    for i in range(29,-1,-1):
        answer.append(str(1<<i))
        
    print(" ".join(answer))
    return

final_result = []

t = get_int()

for _ in range(t):
    n = get_int()
    a = get_list_int()
    solve(n,a)
