import sys
from os import path
from collections import deque

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

def solve(n):
    binary = deque(list(str(bin(n))[2:]))
    binary.appendleft("0")
    ans = []
    carry = False
    
    for i in range(len(binary)-1, 0, -1):
        if carry:
            if binary[i-1] == "1":
                binary[i-1] = "0"
            else:
                binary[i-1] = "1"
                carry = False
                
        if binary[i] == "1" and binary[i-1] == "1":
            binary[i-1] = "0"
            carry = True
            ans.append("-1")
        else:
            ans.append(binary[i])

    if binary[0] == "1":
        ans.append(binary[0])
    
    return len(ans), " ".join(ans)


t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    ans1, ans2 = solve(n)
    final_result.append(str(ans1))
    final_result.append(str(ans2))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

