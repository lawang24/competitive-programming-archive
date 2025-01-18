import sys
from collections import deque
from collections import Counter
import math
import heapq
sys.set_int_max_str_digits(5040)

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
    n, d = get_list_int()
    ans = []
    
    n = min(n, 6)
    
    digits = math.factorial(n)
    num = int(digits * str(d))
    
    for i in range(1,10,2):
        if num%i == 0:
            ans.append(i)
    printNumArr(ans)
    
        
    