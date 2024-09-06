import sys
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

def find_closest(options, number, target):
    local_champ = 0
    for i in options:
        if i!=0:
            diff1 = (target-number) % i
            local_champ = max(diff1,local_champ)
    return local_champ

def solve(a,b,nums):
    options = [a,b,b-a]
    _max = max(nums)
    champ = 0
    for f in range(_max,_max+b):
        for num in nums:
            champ = max(champ, find_closest(options, num, f)) 
    return champ

t = get_int()
final_result = []

for _ in range(t):
    n, a, b = get_list_int()
    if b<a:
        a,b = b,a
    nums = get_list_int()
    ans = solve(a,b,nums)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

