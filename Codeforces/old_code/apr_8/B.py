import sys
from os import path
from collections import Counter

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


def solve(n, c, d, arr):
    
    a = min(arr)
    
    count = Counter(arr)
    
    for i in range(0,n):
        for j in range(0,n):
            num = i*d + j*c + a
            if count[num]:
                count[num]-=1
            else:
                return "NO"

    return "YES"


t = get_int()

final_result = []

for _ in range(t):
    n,c,d = get_list_int()
    arr = get_list_int()
    ans = solve(n, c, d, arr)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

