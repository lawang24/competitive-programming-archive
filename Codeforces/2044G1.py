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
    
# use tortoise and hare on each one

t = get_int()

for _ in range(t):
    n = get_int()
    a = get_list_int()
    
    # adjust for indexing
    a = [0] + a
    n+=1
    
    seen = [False for _ in range(n)]
    distance = [0 for _ in range(n)]
    champ = 0
    
    for i in range(1,n):
        if seen[i]:
            continue
        
        slow = fast = i
        count = 0
        flag = False
        
        # there must be a cycle
        while True:
            slow = a[slow]
            count+=1
            if seen[slow]:
                flag = True
                count+=distance[slow]
                break
            for _ in range(2):
                fast = a[fast]
            if slow == fast:
                break
            
        if flag:
            tracker = count
            ptr = i
            for _ in range(count):
                distance[ptr] = tracker
                ptr = a[ptr]
                tracker-=1
                seen[ptr] = True
            champ = max(champ, count)
            continue
        
        # find the number of steps until cycle
        slow = i
        count = 0
        seen[slow] = seen[fast] = True
        while slow!=fast:
            slow = a[slow]
            fast = a[fast]
            seen[slow] = seen[fast] = True
            count+=1
            
        # mark entire cycle as seen
        head = slow
        seen[head] = True
        slow = a[slow]
        while slow!=head:
            seen[slow] = True
            slow = a[slow]
            
        ptr = i
        tracker = count
        for _ in range(count):
            seen[ptr] = True
            distance[ptr] = tracker
            ptr = a[ptr]
            tracker-=1
            
        champ = max(champ, count)
      
    print(champ+2)  
