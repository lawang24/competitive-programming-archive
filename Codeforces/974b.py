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

final_result = []

t = get_int()

for _ in range(t):
    n, k = get_list_int()
    if (k+n%2)//2%2:
        print("NO")
    else:
        print("YES")
    
            