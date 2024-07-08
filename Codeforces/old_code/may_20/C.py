import sys
from os import path
import collections

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

def solve(n,nums):
    one_two = collections.defaultdict(int)
    two_three = collections.defaultdict(int)
    one_three = collections.defaultdict(int)
    seen = collections.defaultdict(int)
    
    count = 0
    
    for j in range(1,n-1):
        f, s, t = nums[j-1], nums[j], nums[j+1]
        count-=seen[(f,s,t)]*3
        count+=one_two[(f,s)]
        count+=two_three[(s,t)]
        count+=one_three[(f,t)]
        one_two[(f,s)]+=1
        two_three[(s,t)]+=1
        one_three[(f,t)]+=1
        seen[(f,s,t)]+=1
        
    return count

cases = get_int()

final_result = []

for _ in range(cases):
    n = get_int()
    nums = get_list_int()
    ans = solve(n, nums)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

