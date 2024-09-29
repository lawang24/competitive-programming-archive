import sys
from collections import Counter
from string import ascii_lowercase

FILE = 0 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, s):
    
    total = [Counter(), Counter()]
    
    # count total even and odd
    for i in range(n):
        total[i%2][s[i]]+=1
        
    # if even, don't delete anything
    # if you deleted, you could have also just changed those two characters to your end goal
    if n % 2 == 0:
        return n-total[0].most_common()[0][1]-total[1].most_common()[0][1]
    
    champ = n
    
    # if odd, try to delete each letter
    prefix = [Counter(), Counter()]
    for i in range(n):
        # can't use this one for this iteration
        total[i%2][s[i]]-=1
        
        not_replaced = 0
         
        # test each letter for even & odd
        
        for j in range(2):
            alternating_max = 0
            for letter in ascii_lowercase:
                # take the maximum letter for this alternation
                alternating_max = max(alternating_max,prefix[j%2][letter] + total[(j+1)%2][letter]-prefix[(j+1)%2][letter])
            not_replaced+=alternating_max
        
        champ = min(n-not_replaced, champ)
                
        # count this letter permanently
        prefix[i%2][s[i]]+=1
        # reset
        total[i%2][s[i]]+=1
        
    return champ
        

final_result = []

t = get_int()

for _ in range(t):
    n = get_int()
    s = get_string()
    final_result.append(str(solve(n, s)))
    

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

