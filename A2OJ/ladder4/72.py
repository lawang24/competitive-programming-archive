import sys
from os import path

FILE =  0 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(points):
    coordinates = []
    for i in range(len(points)-1):
        u, v = points[i], points[i+1]
        if v<u:
            u, v = v, u
        coordinates.append((u, v))
    
    coordinates.sort(key = lambda x: (x[0], -x[1]))
    print(coordinates)
    
    last = [float("inf")]
    
    for start, end in coordinates:
        while start>=last[-1]:
            last.pop()
        if end<last[-1]:
            last.append(end)
        if end>last[-1]:
            return "yes"
        
    return "no"
            
t = get_int()

points = get_list_int()
ans = solve(points)
sys.stdout.write(str(ans))

