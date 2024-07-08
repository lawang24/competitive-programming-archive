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

def solve(num):
    
    champ=(0,0)
    for i in range(2,num+1):
        j = 1
        count = 0
        while j*i <= num:
            count+=j*i
            j+=1
        if count>champ[0]:
            champ = (count, i)
    return champ[1]

t = get_int()

final_result = []

for _ in range(t):
    num = get_int()
    ans = solve(num)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

