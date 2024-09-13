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

def solve(nums, modifier):
    rem = sorted([nums[i]%modifier for i in range(len(nums))])
    
    champ = rem[-1]-rem[0]
    
    for i in range(1,n):
        champ = min(champ, rem[i-1]+modifier-rem[i])
        
    return champ
   

t = get_int()
final_result = []

for _ in range(t):
    n, a, b = get_list_int()
    modifier = math.gcd(a,b)
    nums = get_list_int()
    ans = solve(nums, modifier)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

