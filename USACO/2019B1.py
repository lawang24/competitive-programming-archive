import sys

FILE = 0 # if needed change it while submitting

if not FILE:
    sys.stdin = open('herding.in', 'r')
    sys.stdout = open('herding.out', 'w')
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(a,b,c):
    left_diff , right_diff = b-a-1, c-b-1
    
    if left_diff == 0 and right_diff == 0:
        minimum = 0
    elif left_diff ==1 or right_diff == 1:
        minimum = 1
    else:
        minimum = 2
        
    maximum = max(left_diff, right_diff)
    
    return minimum, maximum
  
a, b, c = sorted(get_list_int())
ans = solve(a,b,c)

for num in ans:
    print(str(num))
    

