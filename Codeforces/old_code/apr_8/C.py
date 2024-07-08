import sys
from os import path
from collections import deque

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

def solve(n, k, ships):
    
    if k>=sum(ships):
        return n
    
    ans = 0
    
    while n > 1 and k >= min(ships[0],ships[-1]) * 2:
        
        smaller = min(ships[0], ships[-1])
        
        ships[0]-=smaller
        ships[-1]-=smaller
        k-=smaller*2
        
        if ships[0] == 0:
            ans+=1
            ships.popleft()
            n-=1
        
        if ships[-1] == 0:
            ans+=1
            ships.pop()
            n-=1
            
    if k//2 + k%2 == ships[0]:
        ans+=1
    
    return ans

t = get_int()

final_result = []

for _ in range(t):
    n, k = get_list_int()
    ships = deque(get_list_int())
    ans = solve(n, k, ships)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

