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

# def solve():

t = get_int()

final_result = []

for _ in range(t):
    ans = []
    n, m = get_list_int()
    _max = max(get_list_int())
    for _ in range(m):
        op = get_string().split()
        l, r = int(op[1]), int(op[2])
        if op[0] == "+" and l<=_max<=r:
            _max+=1
        elif l<=_max<=r:
            _max-=1
        ans.append(str(_max))
    final_result.append(" ".join(ans))
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

