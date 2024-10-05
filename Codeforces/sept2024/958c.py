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
    _bin = list(bin(n))
    ans = [str(n)]
    for i in range(len(_bin)-1, 1, -1):
        if _bin[i] == '0':
            continue
        new = _bin[:]
        new[i] = '0'
        new_num = int("".join(new),0)
        if new_num:
            ans.append(str(new_num))
    print(len(ans))
    print(" ".join(reversed(ans)))    


