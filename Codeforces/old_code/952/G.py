import sys

mod = (10**9 + 7)

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

def geometricSum(a, multiply, n):
    if n<0:
        return 0
    return (a*(1-multiply**n)//(1-multiply)) % mod

def solve(l, r, k):
    
    if k>9:
       return 0
   
    options = (9//k)+1
    
    ans = 0
    
    a = options-1
    multiplier = options
    n1 = r
    
    ans = geometricSum(a,multiplier,n1) - geometricSum(a,multiplier,l)
    
    # for digits in range(l+1,r+1):
    #     ans += (options-1)*options**(digits-1)
    #     ans %= mod
   
    return ans % mod
    
t = get_int()

final_result = []

for _ in range(t):
    l, r ,k = get_list_int()
    ans = solve(l, r, k)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n') 

