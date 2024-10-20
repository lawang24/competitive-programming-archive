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
    s1, s2 = get_string(), get_string()
    
    # s2 is longer
    if len(s1) > len(s2):
        s2, s1 = s1, s2
        
    i = 0
    while i< len(s1) and s1[i] == s2[i]:
        i+=1
    
    ans = min(len(s1) + len(s2),len(s1) + len(s2) - i + 1)
    print(ans)