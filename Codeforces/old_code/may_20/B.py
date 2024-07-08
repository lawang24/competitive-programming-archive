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

def solve(n,s):
    letters = set()
    for c in s:
        letters.add(c)
    sorted_letters = sorted(letters)
    i , j = 0, len(sorted_letters)-1
    
    mapping = {}
    
    while i<=j:
        mapping[sorted_letters[i]] = sorted_letters[j]
        mapping[sorted_letters[j]] = sorted_letters[i]
        i+=1
        j-=1
        
    ans = []
    
    for c in s:
        ans.append(mapping[c])
    
    return "".join(ans)


t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    s = get_string()
    ans = solve(n, s)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

