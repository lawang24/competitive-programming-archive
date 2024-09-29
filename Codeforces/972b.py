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

def solve(t1, t2, david,n):
    if david<t1:
        return t1-1
    if david > t2:
        return n-t2
    return (t2-t1)//2
    
    

final_result = []
t = get_int()

for _ in range(t):
    n, m , q = get_list_int()
    t1, t2 = get_list_int()
    if t2<t1:
        t1, t2 = t2, t1
    david = get_int()
    final_result.append(str(solve(t1, t2, david, n)))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

