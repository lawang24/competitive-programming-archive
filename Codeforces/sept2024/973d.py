import sys
import math

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

def solve(n,a):
    
    _min = math.inf
    total = 0
    for i, c in enumerate(a,1):
        total += c
        _min = min(_min, total // i) 
        
    _max = 0
    total = 0
    for i, c in enumerate(reversed(a),1):
        total += c
        _max = max(_max, math.ceil(total / i)) 
        
    return _max - _min
    
final_result = []

t = get_int()
for _ in range(t):
    n = get_int()
    a = get_list_int()
    final_result.append(str(solve(n,a)))
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

