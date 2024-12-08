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
    switches = Counter(get_list_int())
    
    _min = 0 
    if switches[1]%2 == 1 and switches[0] % 2 == 1:
        _min = 1
    _max = min(switches[1], switches[0])
    print(_min, _max)