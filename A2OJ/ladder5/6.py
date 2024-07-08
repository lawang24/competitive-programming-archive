import sys
from os import path

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

def solve(nums):
    reversed = False
    i = 0
    left = right = 1
    while i<n-1:
        if nums[i]>nums[i+1]:
            if reversed:
                return "no"
            j = i+1
            # get to rightmost
            while j<n and nums[j-1] > nums[j]:
                j+=1
            if i==0 and j==n:
                return ("yes", i+1, j)
            if i==0 and nums[i] > nums[j]:
                return "no"
            if j==n and nums[i-1]>nums[j-1]:
                return "no"
            if i!=0 and j!=n and (nums[i]>nums[j] or nums[i-1] > nums[j]):
                return "no"
            left = i+1
            right = j
            reversed = True
            i = j
        else:
            i+=1
    
    return ("yes", left, right)

n = get_int()

final_result = []

nums = get_list_int()
ans = solve(nums)

if len(ans) == 3:
    sys.stdout.write("yes")
    sys.stdout.write('\n')
    sys.stdout.write(f'{ans[1]} {ans[2]}')
else:
    sys.stdout.write("no")

