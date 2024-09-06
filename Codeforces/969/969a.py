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

def solve(l, r):
    i = l
    ans = 0
    while i <= r-2:
        if i%2==0:
            i+=1
            continue
        ans+=1
        i+=3
    return ans
        
t = get_int()
final_result = []


for _ in range(t):
    l, r = get_list_int()
    ans = solve(l,r)
    final_result.append(str(ans))
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

