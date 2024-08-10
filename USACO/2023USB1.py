import sys

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, string):
    
    not_F_positions = [i for i in range(n) if string[i]!="F"]
    
    tail_Fs = n - (not_F_positions[-1]-not_F_positions[0]+1)
    
    min = 0
    max = 0
    
    for i in range(len(not_F_positions)-1):
        
        # endings are the same
        if string[not_F_positions[i]] == string[not_F_positions[i+1]]:
            if (not_F_positions[i+1]-not_F_positions[i]) %2 == 0:
                max+=
                
        BEEB
        BEB
        BB
            
    
    
    
    
    return
    
n = get_int()
string = get_string()

sys.stdout.write(str(solve(n, string)))

