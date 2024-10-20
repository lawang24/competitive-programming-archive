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

def solve(n, m, members, slides):
    memberidx = 0
    seen = set()
    for s in slides:
        # use this guy 
        if s == members[memberidx]:
            seen.add(s)
            if memberidx < n-1:
                memberidx+=1
        # can't use this guy or previous guys
        elif s not in seen:
            print('TIDAK')
            return
    
    print('YA')
        
t = get_int()

for _ in range(t):
    n, m, q = get_list_int()
    members = get_list_int()
    slides = get_list_int()
    solve(n, m, members, slides)