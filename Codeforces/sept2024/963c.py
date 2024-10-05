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

def solve(n, k, times):
    _max = min(times), max(times)
    mod = 2*k
    l, r = 0, mod
    
    for i in range(n):
        nl = times[i] % mod
        nr = (nl + k) % mod
        if nr < nl:
            l = max(l, nr)
            r = min(r, nl)
        else:
            l , r = max(l, nl), min(nr, r)
        if r<=l:
            return -1
        print(times[i],l, r)
    
    return _max - (_max % mod) + l
        
final_result = []

t = get_int()

for _ in range(t):
    n, k = get_list_int()
    times = get_list_int()
    ans = str(solve(n, k, times))
    final_result.append(ans)

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

