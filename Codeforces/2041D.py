import sys
from collections import deque
from collections import Counter
import math
import heapq

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

def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))
    
def solve():
    queue = deque()
    
    # [row][col][dir][consecutive][steps]
    steps = [[[[math.inf for _ in range(4)] for _ in range(4)] for _ in range(m)] for _ in range(n)]
    
    end = None
    
    # find the starting and ending coordinates
    # set the initial state for starting
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'T':
                end = (i,j)
            if maze[i][j] == 'S':
                for direction in range(4):
                    steps[i][j][direction][0] = 0
                    queue.append((i, j, direction, 0))
                
    while queue:
        x, y, _dir, consecutive = queue.popleft()
        if (x, y) == end:
            print(steps[x][y][_dir][consecutive])
            return
        
        for new_dir in range(4):
            dx, dy = DIR[new_dir]
            nx, ny = x+dx, y+dy
            # new position is valid
            if not (0<=nx<n and 0<=ny<m and maze[nx][ny]!='#'):
                continue
            # 3 consecutive rule
            if _dir == new_dir:
                if consecutive == 3:
                    continue
                new_cons = consecutive+1                    
            else:
                new_cons = 1
                
            old_val = steps[nx][ny][new_dir][new_cons]
            new_val = steps[x][y][_dir][consecutive] + 1
            if new_val < old_val:
                steps[nx][ny][new_dir][new_cons] = new_val
                queue.append((nx, ny, new_dir, new_cons))
            
    
    print(-1)
    
    
    

DIR = [(1,0), (-1, 0), (0, 1), (0, -1)]

n, m = get_list_int()
maze = []

for _ in range(n):
    maze.append(list(get_string()))
    
solve()
        
