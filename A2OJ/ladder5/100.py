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

def solve(n, matrix, final_result):
    
    a = [[0 for _ in range(n)] for _ in range(n)]
    b = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(i,n):
            average = (matrix[i][j] + matrix[j][i]) / 2 
            a[i][j] = average
            a[j][i] = average
            b[i][j] = matrix[i][j] - average
            b[j][i] = matrix[j][i] - average
    
    for row in a:
        final_result.append(' '.join(str(x) for x in row))
        
    for row in b:
        final_result.append(' '.join(str(x) for x in row))
        
t = get_int()

final_result = []
matrix = []

for _ in range(t):
    row = get_list_int()
    matrix.append(row)
    
solve(t, matrix, final_result)

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

