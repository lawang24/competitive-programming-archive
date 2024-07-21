import sys

sys.stdin = open('hoofball.in', 'r')
sys.stdout = open('hoofball.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, cows):
    
    cows.sort()
    directions = [0 for _ in range(n)]
    directions[0] = 1
    directions[-1] = -1
    
    for i in range(1, n-1):
        if cows[i+1]-cows[i] < cows[i] - cows[i-1]:
            directions[i] = 1
        else:
            directions[i] = -1
            
    balls = 1
    
    used = [0 for _ in range(n)]
    
    for i in range(1,n):
        
        # source balls 
        if directions[i] == 1 and directions[i-1] != 1:
            balls +=1
        if directions[i] == 
        
        
        # last ball was right
        # either cycle or pass on
            balls+=1
        
        if directions[i] == -1 and directions[i]
        
        if directions[i] == -1:
            # this cell creates used cycle
            if i>1 and directions[i-1] == 1 and directions[i-2] == 1:
                used[i] = 1
            
            # adding a new block to cycle
            if used[i-1] == 1:
                balls+=1
                
    return balls
        
n = get_int()
cows = get_list_int()
    
sys.stdout.write(str(solve(n, cows)))