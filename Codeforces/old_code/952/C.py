import sys

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
    champ = 0
    ans = 0
    
    sums = [0 for _ in range(len(nums))]
    
    for i in range(len(sums)):
        if i:
            sums[i] = sums[i-1]+nums[i]
        else:
            sums[i] = nums[i]
        champ = max(champ, nums[i])
        if sums[i]-champ == champ:
            ans+=1
            
    return ans

t = get_int()

final_result = []

for _ in range(t):
    _ = get_int()
    nums = get_list_int()
    ans = solve(nums)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

