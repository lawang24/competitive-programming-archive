import sys

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

def solve(x, y, k):
    
    x_coord, y_coord = [], []
    
    if k%2 == 1:
        x_coord.append(x)
        y_coord.append(y)
        k-=1
        
    count = 1
    for _ in range(0, k, 2):
        x_coord.append(x+count)
        x_coord.append(x-count)
        y_coord.append(y+count)
        y_coord.append(y-count)
        count+=1
        
    for i in range(len(x_coord)):
        final_result.append(f'{x_coord[i]} {y_coord[i]}')

t = get_int()

final_result = []

for _ in range(t):
    x, y, k = get_list_int()
    solve(x, y, k)

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

