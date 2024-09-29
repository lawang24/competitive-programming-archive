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
    n = get_int()
    a = get_list_int()
    if n <=2:
        final_result.append("-1")
        continue
    
    a.sort()
    middle = a[n // 2]
    ans = middle * 2 * n - sum(a)
    if ans < 0 :
        ans = 0
    else:
        ans+=1
    final_result.append(str(ans))
    
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

