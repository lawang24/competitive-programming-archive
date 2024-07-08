import sys
from os import path
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

def solve(word):
    
    last_num = 0
    last_letter = "a"
        
    
    for i, v in enumerate(word):
        
     
        if v.isdigit():
            if (i>0 and not word[i-1].isdigit()) or int(v) < last_num:
                return "NO"
            last_num = int(v)
        else:
            if v < last_letter:
                return "NO"
            last_letter = v
        
        
    return "YES"

t = get_int()


final_result = []

for _ in range(t):
    n = get_int()
    word = get_string()
    ans = solve(word)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

