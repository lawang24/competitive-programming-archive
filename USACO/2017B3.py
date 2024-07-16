import sys

sys.stdin = open('art.in', 'r')
sys.stdout = open('art.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, grid):
    usable = set()
    visited = set()
    
    for row in grid:
        curr = 0
        seen = set()
        for val in row:
            if val not in visited:
                usable.add(val)
                visited.add(val)
                
            # part of rectangle
            if curr!=val:
                if val not in seen:
                    seen.add(val)
                elif val in usable:
                    usable.remove(val)
            curr = val
            
    if 0 in usable:
        usable.remove(0)
        
    return usable

side_length = get_int()
grid = []
for _ in range(side_length):
    grid.append(list(get_string()))


    
set1 = solve(side_length,grid)
set2 = solve(side_length,zip(*grid))
print(set1)
print(set2)
ans = len(set1 & set2) 
sys.stdout.write(str(ans))