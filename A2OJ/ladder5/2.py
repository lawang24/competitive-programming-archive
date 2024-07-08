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


def solve(n,m,tasks):
    curr = 1
    total_time = 0 
    for task in tasks:
        if task<curr:
            total_time += n+task-curr
        else:
            total_time += task-curr
        curr =
    return total_time

final_result = []

n, m = get_list_int()
tasks = get_list_int()
ans = solve(n, m, tasks)
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

