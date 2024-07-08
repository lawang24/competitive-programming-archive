import sys

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

def getNextTurn(lastTurn):
    x, y = lastTurn[0], lastTurn[1]
    if x==y:
        if y<=0:
            return (-x+1,y)
        elif x<=0:
            return (x, -y)
        else:
            return (-x,y)
    else: return (x,x)

def solve(x, y):
    DIR = [(1,0),(0,1) ,(-1,0), (0, -1)]
    turns = 0
    curr_x = 0
    curr_y = 0
    last_turn = (1,0)
    i = 0
    
    while not (curr_x ==x and curr_y ==y):
       
        if (curr_x, curr_y) == last_turn:
            turns+=1
            last_turn = getNextTurn(last_turn)
            i+=1
            
        dx, dy = DIR[i%4]
        curr_x+=dx
        curr_y+=dy
        
    return turns


final_result = []

x, y = get_list_int()
ans = solve(x, y)
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

