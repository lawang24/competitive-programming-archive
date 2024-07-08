import sys

sys.stdin = open('sleepy.in', 'r')
sys.stdout = open('sleepy.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(ncows, lineup):
    i = ncows-1
    
    # find latest non-sorted pair of cows
    while i>0:
        if lineup[i-1] > lineup[i]:
            break
        i-=1
        
    return i
    
ncows = get_int()
lineup = get_list_int()
sys.stdout.write(str(solve(ncows, lineup)))