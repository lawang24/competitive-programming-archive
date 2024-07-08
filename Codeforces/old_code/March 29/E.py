import sys
from os import path

FILE = False # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_shortest_repeating(word, n):
    
    # checking all possible divisor strings
    for len_k in range(1,n+1):
        
        # valid divisors only
        if n%len_k != 0:
            continue
        
        errors = 0
        
        # check prefix
        for i in range(n):
            if word[i] != word[(i%len_k)]:
                errors+=1
            if errors>1:
                break
            
        if errors <= 1:
            return len_k
        
        errors = 0
        
        # check suffix
        for i in range(n):
            if word[i] != word[(i%len_k)-len_k]:
                errors+=1
            if errors>1:
                break
            
        if errors <= 1:
            return len_k
        
    return "not right"

n = get_int()

final_result = []
for _ in range(n):
    n = get_int()
    word = get_string()
    ans = get_shortest_repeating(word, n)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

