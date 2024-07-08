import sys
from os import path

FILE =  1

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

t = 5

row, col = 0, 0

for i in range(t):
    curr_row = get_list_int()
    if 1 in curr_row:
        row = i
        col = curr_row.index(1)

sys.stdout.write(str(abs(row-2)+abs(col-2)))

