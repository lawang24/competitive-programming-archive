import sys
import math

sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(cows):
    i = 0
    ans = 0
    while i < len(cows)-1:
        if cows[i]>cows[i+1]:
            cows[i], cows[i+1] = cows[i+1], cows[i]
            ans += 1
            i = -1
        i+=1
        
    return ans
        
n = get_int()
cows = []
for _ in range(n):
    new_cow = get_int()
    if not cows or new_cow != cows[-1]:
        cows.append(new_cow)

sys.stdout.write(str(solve(cows)))