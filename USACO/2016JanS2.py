import sys
sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

n = get_int()
first = [-1 for _ in range(7)]
champ = 0
curr = 0

for i in range(n):
    curr+=get_int()
    curr%=7
    if first[curr] != -1:
        champ = max(champ, i-first[curr])
    else:
        first[curr] = i
            
sys.stdout.write(str(champ))