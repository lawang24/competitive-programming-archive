import sys
from os import path
from collections import Counter

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

def solve(a,b,n, m):
    
    max_misses = m-k
    
    ans = 0
    b_count = Counter(b)
    misses = 0
    
    # initialize
    for v in a[:len(b)]:
        if b_count[v] <= 0:
            misses+=1
        b_count[v]-=1
        
        
    if misses <= max_misses:
        ans+=1
        
    i , j = 0, len(b)
    
    while j<len(a):
        
        # handle left
        if b_count[a[i]]<0:
            misses-=1
        b_count[a[i]]+=1
        
        if b_count[a[j]] <= 0:
            misses+=1
        b_count[a[j]] -=1
        
        if misses <= max_misses:
            ans+=1
        
        i+=1
        j+=1
    
    return ans
        

t = get_int()

final_result = []

for _ in range(t):
    n, m, k = get_list_int()
    a = get_list_int()
    b = get_list_int()
    ans = solve(a,b, n, m)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

