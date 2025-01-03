import sys
from collections import deque
from collections import Counter
import math
import heapq

FILE = 1  # if needed change it while submitting

if FILE:
    sys.stdin = open("Codeforces/input.txt", "r")
    sys.stdout = open("Codeforces/output.txt", "w")

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int, get_string().split()))


def printArr(arr):
    print(" ".join([str(x) for x in arr]))


t = get_int()

for _ in range(t):
    n, q = get_list_int()
    a = get_list_int()
    K = math.floor(math.log2(n))

    # find the gcds between numbers
    for i in range(n - 1):
        a[i] = abs(a[i + 1] - a[i])

    # redefine sizes
    a.pop()
    n -= 1
    sparse_table = [[0 for _ in range(n)] for _ in range(K + 1)]

    for i in range(n):
        sparse_table[0][i] = a[i]

    # 1 << log2_len
    log2_len = 1
    while log2_len <= K:
        for j in range(0, n - (1 << log2_len) + 1):
            l = sparse_table[log2_len - 1][j]
            r = sparse_table[log2_len - 1][j + (1 << (log2_len - 1))]
            sparse_table[log2_len][j] = math.gcd(l, r)
        log2_len += 1

    
    ans = []
    # query the sparse table
    for _ in range(q):
        l, r = get_list_int()
        
        if l == r:
            ans.append(0)
            continue
    
        l -= 1
        r -= 2
        log2_interval = math.floor(math.log2(max(1,r - l + 1)))
        left_min = sparse_table[log2_interval][l]
        right_min = sparse_table[log2_interval][r - (1 << log2_interval) + 1]
        ans.append(math.gcd(left_min, right_min))

    printArr(ans)