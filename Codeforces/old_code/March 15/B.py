import sys
from os import path

FILE = False # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def canFix(n_array):
    
    last = 0
    
    for num in n_array:
        if num < last:
            return "No"
        tens = num//10
        ones = num%10
        # tens digit greater than ones
        if tens > ones:
            last = num
        elif tens >= last or num < 10:
            last = ones
        else:
            last = num
            
    return "Yes"
    
n = get_int()

final_result = []
for i in range(n):
    t = get_int()
    numbers = list(map(int,get_string().split(" ")))
    ans = canFix(numbers)
    final_result.append(ans)

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

