import sys
from collections import Counter
import heapq
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

mod = 10**9 + 7

def solve(n, nums):
    curr_sum = 0
    ans = 0
    for i in range(n):
        ans += nums[i] * curr_sum % mod
        curr_sum += nums[i] % mod
    divisor = math.comb(n,2) 
    inv_mod = pow(divisor, mod-2, mod)
    return (ans * inv_mod) % (mod)

t = get_int()

for _ in range(t):
    n = get_int()
    nums = get_list_int()
    print(str(solve(n, nums)))