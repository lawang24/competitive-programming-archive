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
    
    
if __name__ == '__main__':   
    t = get_int()

    for _ in range(t):
        n = get_int()
        arr = get_list_int()
        champ = sum(arr)
        
        while len(arr) > 1:
            champ = max(arr[0]-arr[-1], arr[-1]-arr[0], champ)
            for i in range(len(arr)-1):
                arr[i] = arr[i+1] - arr[i] 
            arr.pop()
        
        print(champ)
    