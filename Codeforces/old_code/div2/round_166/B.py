import sys
from os import path
import math

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, a, b):
    reached = False
    extra_num = b[-1]
    ans = 0
    closest = math.inf
    
    for i in range(n):
        if b[i] < a[i]:
            b[i], a[i] = a[i], b[i]
        ans+=b[i]-a[i]
        if a[i] <=extra_num<= b[i]:
            reached = True
        if not reached:
            closest = min(closest, abs(extra_num-a[i]), abs(extra_num-b[i]))
        
    if not reached:
        ans+=closest
        
    return ans+1

t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    a = get_list_int()
    b = get_list_int()
    ans = solve(n, a, b)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

