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

def median(nums, n):
    nums.sort()
    median_idx = (n+1)//2 -1
    left ,right =  median_idx, median_idx
    
    while right<n-1 and nums[right+1] == nums[right]:
        right+=1
    
    return right-left+1

t = get_int()

final_result = []
for i in range(t):
    n = get_int()
    nums = list(map(int,get_string().split()))
    final_result.append(str(median(nums, n)))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

