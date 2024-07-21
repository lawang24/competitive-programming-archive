import sys

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, k, days):
    total = 1+k
    
    for i in range(1,n):
        total+=min(1+k, days[i]-days[i-1])
        
    return total

n, k = get_list_int()
days = get_list_int()
    
sys.stdout.write(str(solve(n, k , days)))