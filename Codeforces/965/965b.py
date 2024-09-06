import sys

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

def solve(n,nums):
    return ' '.join([str(nums[i-1]) for i in range(n)])

t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    nums = get_list_int()
    final_result.append(solve(n, nums))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

