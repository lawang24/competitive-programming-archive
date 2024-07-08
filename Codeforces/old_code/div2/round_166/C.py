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

def solve(n, m, a, b):
    programmers = []
    testers = []
    fake_programmers = []
    fake_testers = []
    ans = []
    total = 0
    roles = ["" for _ in range(n+m+1)]
    
    for i in range(n+m+1):
        if a[i] > b[i]:
            if len(programmers) == n:
                fake_testers.append(i)
                roles[i] = "ft"
                total+=b[i]
            else:
                programmers.append(i)
                roles[i] = "p"
                total+=a[i]
        else:
            if len(testers) == m:
                fake_programmers.append(i)
                roles[i] = "fp"
                total+=a[i]
            else:
                testers.append(i)
                roles[i] = "t"
                total+=b[i]
                
    for i in range(n+m+1):
        count = total
        if roles[i] == "p":
            if fake_testers:
                idx = fake_testers[0]
                count+= a[idx]-b[idx]
            count-=a[i]
        if roles[i] == "t":
            if fake_programmers:
                idx = fake_programmers[0]
                count+= b[idx]-a[idx]
            count-=b[i]
        if roles[i] == "fp":
            count-=a[i]
        if roles[i] == "ft":
            count-=b[i]
        
        ans.append(str(count))
        
    return " ".join(ans)

t = get_int()

final_result = []

for _ in range(t):
    n, m = get_list_int()
    a = get_list_int()
    b = get_list_int()
    ans = solve(n, m, a, b)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

