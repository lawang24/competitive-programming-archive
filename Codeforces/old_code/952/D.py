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

def solve(m, n, grid):
    heights = []
    widths = []
    
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "#":
                heights.append(str(row+1))
                widths.append(str(col+1))
    
    return heights[len(heights)//2]+ " " +  widths[len(widths)//2]

t = get_int()

final_result = []

for _ in range(t):
    m, n = get_list_int()
    grid = []
    for _ in range(m):
        line = list(get_string())
        grid.append(line)
    ans = solve(m, n, grid)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

