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

def solve(n, x ):
    ans = 0
    for a in range(1,n):
        b = 1
        while (a*b <= n):
            c = min(x-a-b, (n-a*b)//(a+b))
            if c > 0:
                ans+=c
            b+=1
    return ans

final_result = []

t = get_int()

for _ in range(t):
    n, x = get_list_int()
    final_result.append(str(solve(n, x)))
    
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

