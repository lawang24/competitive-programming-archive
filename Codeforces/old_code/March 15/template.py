import sys
from os import path

FILE = False # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

n = get_int()

final_result = []
for i in range(n):
    word = get_string()
    final_result.append(word.upper())

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

