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

def solve(x, y, z, k):
    champ = 0
    
    for a in range(1,x+1):
        if k%a!=0:
            continue
        for b in range(1, y+1):
            if (k//a)%b!=0:
                continue
            for c in range(1, z+1):
                if a*b*c == k:
                    champ = max(champ, (x-a+1)*(y-b+1)*(z-c+1) )
                    
    return champ

t = get_int()

final_result = []

for _ in range(t):
    x, y, z, k = get_list_int()
    ans = solve(x, y, z, k)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

