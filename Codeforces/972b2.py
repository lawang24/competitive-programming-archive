import sys
import bisect

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

def solve(teachers, davids, n):
    teachers.sort()
    for d in davids:
        if d<teachers[0]:
            print(teachers[0]-1)
            continue
        if d>teachers[-1]:
            print(n-teachers[-1])
            continue
        pos = bisect.bisect(teachers, d)
        print((teachers[pos]-teachers[pos-1])//2)
    
final_result = []
t = get_int()

for _ in range(t):
    n, m , q = get_list_int()
    teachers = get_list_int()
    davids = get_list_int()
    solve(teachers, davids, n)
