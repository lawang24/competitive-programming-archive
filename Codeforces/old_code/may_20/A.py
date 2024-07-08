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

def solve(x,y):
    count = 0
    
    while x or y:
        screen = 15
        while screen > 7 and y:
            y-=1
            screen-=4
        while screen>0 and x:
            x-=1
            screen-=1
        count+=1
        
    return count


t = get_int()

final_result = []

for _ in range(t):
    x,y = get_list_int()
    ans = solve(x,y)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

