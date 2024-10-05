import sys
import collections

sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve():
    return
    
n, m = get_list_int()
spotty_cows = []
plain_cows = []

for _ in range(n):
    spotty_cows.append(get_string())
    
for _ in range(n):
    plain_cows.append(get_string())
    
healthy_cow_combs = collections.defaultdict(set)

for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):
            _hash = (i,j,k)
            for cow in plain_cows:
                healthy_cow_combs[_hash].add((cow[i],cow[j],cow[k]))
                
count = 0
                
for i in range(m):
    for j in range(i+1,m):
        for k in range(j+1,m):  
            _hash = (i,j,k)
            valid = True
            for cow in spotty_cows:
                if (cow[i],cow[j],cow[k]) in healthy_cow_combs[_hash]:
                    valid = False
                    break
            if valid:
                count+=1

sys.stdout.write(str(count))

