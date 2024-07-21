import sys

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, cows):
    
    curr = "HG"
    flips = 0
    for i in range(n-1, 0, -2):
        
        if curr == "HG" and cows[i-1] == "G" and cows[i] == "H":
            curr = "GH"
            flips+=1
            
        if curr == "GH" and cows[i-1] == "H" and cows[i] == "G":
            curr = "HG"
            flips+=1
    
    return flips

n = get_int()
cows = get_string()

sys.stdout.write(str(solve(n, cows)))