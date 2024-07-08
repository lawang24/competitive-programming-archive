import sys
from os import path

FILE = 1

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))


t = get_int()

sum1 = sum2 = sum3 = 0

for _ in range(t):
    x, y, z = get_list_int()
    sum1+=x
    sum2+=y
    sum3+=z

sys.stdout.write('YES') if sum1==0 and sum2==0 and sum3==0 else sys.stdout.write('NO')
