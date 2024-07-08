import sys
from os import path

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

def solve(n, m):
    if m> n:
        return "No"
    return "Yes" if (m-n)%2 == 0 else "No"
        
t = get_int()

final_result = []

for _ in range(t):
    n, m = get_list_int()
    ans = solve(n, m)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

