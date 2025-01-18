import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")


def get_int():
    return int(sys.stdin.readline())


def get_string():
    return sys.stdin.readline().strip()


def get_list_int():
    return list(map(int, get_string().split()))


def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))


def getHighestFactor(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return num // i
    return 1

t = get_int()

for _ in range(t):
    n, m = get_list_int()
    a = get_list_int()
    a.reverse()
    a = [0] + a
    
    # use 1 indexing for arrays
    ans = [-1 for _ in range(n+1)]
    m_mapping = [-1 for _ in range(n+1)]
    ans[1] = a[1]
    m_mapping[1] = 1
    
    valid = True
    
    for idx in range(2,n+1):
        factor = getHighestFactor(idx)
        value_idx = m_mapping[factor]+1
        if value_idx > m:
            valid = False
            break
        ans[idx] = a[value_idx]
        m_mapping[idx] = value_idx
        
    if valid:
        printNumArr(ans[1:])
    else:
        print(-1)
            

    
        
