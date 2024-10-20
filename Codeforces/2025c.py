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

t = get_int()

for _ in range(t):
    n, k = get_list_int()
    cards = get_list_int()
    cards.sort()
    
    champ = 1
    i = 0
    j = 1
    
    while j < n:
        # print(champ, j)
        # skip duplicates
        if cards[j] == cards[j-1]:
            champ = max(champ, j-i+1)
            j+=1
            continue
        # new sequence start
        if cards[j] > cards[j-1]+1:
            i = j
            j+=1
            continue
        
        # too many uniques
        if cards[j] - cards[i] + 1 > k:
            while cards[i] == cards[i+1]:
                i+=1
            i+=1
            
        champ = max(champ, j-i+1)
        j+=1
    
    
    print(champ)
