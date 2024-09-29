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
    n, d, k = get_list_int()
    brothers = [0 for _ in range(n+1)]
    
    for _ in range(k):
        start, stop = get_list_int()
        brothers[max(1,start-d+1)]+=1
        if stop+1 <= n:
            brothers[stop+1]-=1
            
        
    for i in range(1,n+1):
        brothers[i] += brothers[i-1]
        
    
    bro = (0, 1)
    mom = (math.inf, 1)
    
    for i, v in enumerate(brothers):
        if i == 0 or i>n-d+1:
            continue
        if v < mom[0]:
            mom = (v,i)
        if v > bro[0]:
            bro = (v,i)
            
    final_result.append(f'{bro[1]} {mom[1]}')
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

