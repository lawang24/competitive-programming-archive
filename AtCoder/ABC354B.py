import sys
from os import path

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(word):
    return ans

N = get_int()

final_result = []
users, scores = [], []

for _ in range(N):
    username, rating = get_string().split()
    users.append(username)
    scores.append(int(rating))

users.sort()
winning_idx = sum(scores) % N
ans = users[winning_idx]
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

