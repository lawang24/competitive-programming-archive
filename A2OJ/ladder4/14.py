import sys
from os import path

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

def solve(word):
    words = word.split("WUB")
    str_list = list(filter(None, words))
    return " ".join(str_list)


final_result = []

word = get_string()
ans = solve(word)
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)

