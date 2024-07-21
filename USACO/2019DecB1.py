import sys
import collections

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve():
    return

k, n = get_list_int()

pairs = collections.defaultdict(set)
first = get_list_int()

for i in range(n):
    for j in range(i+1,n):
        pairs[first[i]].add(first[j])

for _ in range(k-1):
    rankings = get_list_int()
    for i in range(n):
        for j in range(i+1,n):
            pairs[rankings[j]].discard(rankings[i])

count = 0

for key in pairs:
    count+=len(pairs[key])

sys.stdout.write(str(count))
    