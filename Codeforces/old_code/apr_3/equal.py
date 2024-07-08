import sys
from os import path
import math

FILE =  1 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def equal(arr):
    
    champ = min(arr)
    
    operations = 0
    rem = [0 for _ in range(5)]
    
    for num in arr:
        i = num-champ
        operations += i//5 + (i%5)//2 + (i%5)%2
        mod = i%5
        rem[mod]+=1
    

    saved = max(0, max(rem[4],rem[3]-rem[1])-rem[2]-rem[0])
    return operations-saved

t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    arr = list(map(int,get_string().split()))
    ans = equal(arr)
    print(ans)
    # final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

