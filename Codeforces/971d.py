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

def solve(n, points, coords):
    ans = 0
    points[0].sort()
    points[1].sort()
    lower_coords, higher_coords = coords
    
    # solve for upright triangles
    for x in points[0]:
        if x in higher_coords:
            ans += n-2
    
    # solve for 90-45-45 triangesl
    for x in points[0]:
        if x+2 in lower_coords and x+1 in higher_coords:
            ans+=1
    for x in points[1]:
        if x+2 in higher_coords and x+1 in lower_coords:
            ans+=1
            
    return ans
    

final_result = []

t = get_int()

for _ in range(t):
    n_points = get_int()
    points = [[],[]]
    coords = [set(), set()]
    for _ in range(n_points):
        x, y = get_list_int()
        points[y].append(x)
        coords[y].add(x)
    final_result.append(str(solve(n_points, points, coords)))
    
for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

