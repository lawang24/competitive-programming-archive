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

def solve(n, instr):
   
    inv = {"W":"E", "E": "W", "N":"S", "S": "N"}
    
    if n==2:
        if instr[0] == instr[1]:
            return "RH"
        return "NO"
    
    hor = 0
    vert = 0
    
    for c in instr:
        if c=="W":
            hor+=1
        if c=="E":
            hor-=1
        if c=="N":
            vert+=1
        if c=="S":
            vert-=1
    
    if hor %2 == 1 or vert%2 == 1:
        return "NO"
    
    ans = ["H" for _ in range(n)]
    
    
    # both 0 case
    if hor == 0 and vert == 0:
        ans[0] = "R"
        ans[instr.index(inv[instr[0]])] = "R"
    else:
        vert_needed = vert//2
        hor_needed = hor//2
        for i,c in enumerate(instr):
            if c=="W" and hor_needed > 0 :
                hor_needed-=1
                ans[i] = "R"
            if c=="E" and hor_needed < 0:
                hor_needed+=1
                ans[i] = "R"
            if c=="N" and vert_needed > 0:
                vert_needed-=1
                ans[i] = "R"
            if c=="S" and vert_needed < 0:
                vert_needed+=1
                ans[i] = "R"
                
    return "".join(ans)
    

cases = get_int()

final_result = []

for _ in range(cases):
    n = get_int()
    instr = get_string()
    ans = solve(n, instr)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

