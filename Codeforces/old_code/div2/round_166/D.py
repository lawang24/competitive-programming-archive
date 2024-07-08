import sys
from os import path
import collections

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

def solve(word):
    lp_count = [1 for _ in range(len(word))]
    rp_count = [1 for _ in range(len(word))]
    ans = 0
    
    count = collections.defaultdict(list)
   
    for i in range(len(word)-2, -1, -1):
        if word[i] == ")":
            rp_count[i] = rp_count[i+1]+1
        else:
            rp_count[i] = rp_count[i+1]-1
    
    for i in range(1,len(word)):
        if word[i] == "(":
            lp_count[i] = lp_count[i-1]+1
        else:
            lp_count[i] = lp_count[i-1]-1
            
        if count[lp_count[i]]:
            for idx in count[lp_count[i]]:
                if rp_count[idx+1]-rp_count[i]>=lp_count[idx]:
                    ans+=1
            
        count[lp_count[i]].append(i)
   
    return ans

t = get_int()

final_result = []

for _ in range(t):
    word = get_string()
    ans = solve(word)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

