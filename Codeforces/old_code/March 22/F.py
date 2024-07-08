import sys
from os import path
import math

FILE = False # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()


def find_height(a,b,c):
    if 1+a!=c:
        return -1
    
    a_length = a.bit_length()
    if a_length == 0:
        return b+c-1
    
    openings = (((1 << a_length) - 1) ^ a)
    remaining_ones = max(0,b-openings)
    
    # 2 openings + 1 openings
    add_routes =  ((1 << a_length-1) - openings) * 2 + openings
    new_height = math.ceil( remaining_ones / add_routes ) if remaining_ones!=0 else 0
    
    height_2 = (a_length-1) 
    # add 1 for zero layer at the end
    min_height = height_2 + new_height + 1
    
    return min_height
    

t = get_int()

final_result = []
for i in range(t):
    numbers = get_string()
    a,b,c = list(map(int,numbers.split()))
    ans = find_height(a,b,c)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

