import sys
from collections import Counter

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

def solve(n, nums):
    _sum = sum(nums)
    
    if _sum % 3 != 0:
        return 0
    
    one_third = _sum // 3
    two_third = one_third * 2
    
    one_third_count = 0
    two_third_count = 0
    curr = 0
    ans = 0

    for i in range(n-1):
        curr+=nums[i]
        if curr == two_third:
            two_third_count+=1
            ans += one_third_count
        if curr == one_third:
            one_third_count+=1
    
    return ans
        

n = get_int()
nums = get_list_int()
print(solve(n, nums))




