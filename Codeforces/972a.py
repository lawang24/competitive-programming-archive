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

def solve(n):
    chars=['a','e','i','o','u']
    times = n//5
    rem = n%5
    ans = []
    
    for c in chars:
        count = times
        if rem:
            count+=1
            rem-=1
        for _ in range(count):    
            ans.append(c)
        
    return "".join(ans)

final_result = []

t = get_int()

for _ in range(t):
    n = get_int()
    final_result.append(solve(n))
    

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

