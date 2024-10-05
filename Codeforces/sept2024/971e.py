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

def solve(n,k):
    
    count = 0
    for i in range(n+1):
        first = i*(i-1)/2 + i*k
        second = (n-i)*k + (n-1)*(n)/2 - (i)*(i-1)/2
        # print('first', first)
        # print('second', second)
        # print(first-second)
        print(i*(i-1)+2*k*i-n*k-(n-1)*n/2)
        
    
    
    
    for i in range(1,n+1):
        total = 2*i*k - n*k - (n-1)*(n) / 2 - i*(i-1) / 2
        # print(total)
    
    i = (n*k - ((n-1)*n)/2 ) / (2 * k)
    # print(i)


final_result = []

t = get_int()

for _ in range(t):
    n, k = get_list_int()
    final_result.append(str(solve(n, k)))
    
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

