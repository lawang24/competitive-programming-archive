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
    
    n = get_list_int()
    a = get_list_int()
    
    MOD = 998244353
    ans = 0
    ones = 0
    twos = 0
    
    for val in a:
        if val == 1:
            ones+=1
            twos+=1
        elif val == 2:
            twos *= 2
            twos %= MOD
        else:
            ans += twos - ones 
            ans %= MOD
            
    print(ans)
                    
            
    
    