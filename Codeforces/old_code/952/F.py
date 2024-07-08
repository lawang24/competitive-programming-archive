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


def solve(h, n, attacks, cooldowns):
    
    
    def canKill(turns):
        damage = 0
        for i in range(n):
            damage+=math.ceil(turns/(cooldowns[i])) * attacks[i]
        return damage >= h
    

    lo, hi = 1, 2**63
    
    while lo<hi:
        mid = (lo+hi)//2
        if canKill(mid):
            hi = mid
        else:
            lo = mid+1
            
    return hi

t = get_int()

final_result = []

for _ in range(t):
    h, n = get_list_int()
    attacks = get_list_int()
    cooldowns = get_list_int()
    ans = solve(h, n, attacks, cooldowns)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

