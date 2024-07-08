import sys
from os import path

FILE =  1 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def count_bits(n):
    count = 0
    while n:
        if n&1:
            count+=1
        n>>=1
    return count

def solve(other_players, fedor, k ):
    ans = 0
    for player in other_players:
        similar = fedor ^ player
        if count_bits(similar)<=k:
            ans+=1
    return ans

n, m, k = get_list_int()

final_result = []
other_players = []

for _ in range(m):
    other_players.append(get_int())

fedor = get_int()
ans = solve(other_players, fedor, k)
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

