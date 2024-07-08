import sys
from os import path

FILE =  # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(bob):
     

t = get_int()

final_result = []

for _ in range(t):
    columns = get_int()
    bob = []
    for _ in range(3):
        bob.append(get_list_int())
    ans = solve(bob)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

