import sys
from collections import deque
from collections import Counter
import math
import heapq
from string import ascii_lowercase

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
    
def solve(s):
    # mid points to last unsafe value
    mid = (len(s)-1) // 2
    safe_middle_count = Counter()
    while mid and s[mid] == s[-(mid+1)]:
        safe_middle_count[s[mid]]+=2
        mid-=1
        
    # overcount on odd
    if len(s) % 2 == 1:
        safe_middle_count[(len(s)-1) // 2] -=1
        
    total_count = Counter(s)
    curr_count = Counter()
    
    for i, v in enumerate(s):
        curr_count[v] += 1
        
        flag = True
        # crossing over now
        if i > mid:
            for letter in ascii_lowercase:
                if curr_count[letter] < total_count[letter] / 2 :
                    flag = False
                    break
        else:
            for letter in ascii_lowercase:
                if curr_count[letter] < (total_count[letter] - safe_middle_count[letter]) / 2:
                    flag = False
                    break
        
        # aaaa bb bbbb
        
        # middle = left_middle + right_middle
        
        # L = left_count + left_middle
        # R = T - L - middle 
        
        # l + x < T - l - x
        
        # L < R
        
        if flag:
            # print(curr_count)
            # print(total_count)
            # print(safe_middle_count)
            return i+1
    
    
t = get_int()

for _ in range(t):
    
    s = get_string()
    i , j = 0, len(s)-1
    
    while i<j and s[i] == s[j]:
        i+=1
        j-=1
    
    # entire sequence is palindrome
    if i >= j:
        print(0)
        continue
    
    s = s[i:j+1]
    
    print(min(solve(s), solve(s[::-1])))
    