import sys

sys.stdin = open('taming.in', 'r')
sys.stdout = open('taming.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(ndays, scores):
    scores[0] = 0
    minimum = 1
    maximum = 1 
    
    for i in range(ndays-1,0,-1):
        # logged non-breakout day
        # prior day is fixed
        if scores[i] > 0:
            if scores[i-1] == -1:
                scores[i-1] = scores[i] - 1
            elif scores[i-1] != scores[i] - 1:
                return -1
        # day is breakout
        elif scores[i] == 0:
            minimum+=1
            maximum+=1
        # day is debatably breakout
        else:
            maximum+=1
            
    return f'{minimum} {maximum}'
        

ndays = get_int()
scores = get_list_int()
sys.stdout.write(str(solve(ndays, scores)))



