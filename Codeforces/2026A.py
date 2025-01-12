import sys
from collections import deque
from collections import Counter
import math
import heapq

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

def printNumArr(arr):
    print(" ".join([str(x) for x in arr]))

t = get_int()

ans = []

for _ in range(t):
    x, y, k = get_list_int()
    
    square_side = min(x,y)
    
    printNumArr([0, 0, square_side, square_side])
    printNumArr([0,square_side,square_side,0])