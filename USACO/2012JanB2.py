import sys

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve():
    return

n, k = get_list_int()
diffs = [0 for _ in range(n+1)]

for _ in range(k):
    l, r = get_list_int()
    diffs[l]+=1
    if r<n:
        diffs[r+1]-=1
        
for i in range(1,n+1):
    diffs[i]+=diffs[i-1]
    
sys.stdout.write(str(sorted(diffs)[len(diffs)//2]))