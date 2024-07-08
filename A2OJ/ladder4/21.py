import sys
from os import path

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, m, a, b):
    if b/m>=a:
        return n*a

    m_count_price =  (n//m) * b
    excess_price = min(b, (n%m) * a)
    return m_count_price + excess_price
    

n, m, a, b = get_list_int()
ans = solve(n, m, a, b)
sys.stdout.write(str(ans))

