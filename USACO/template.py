import sys

sys.stdin = open('name.in', 'r')
sys.stdout = open('name.out', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve():
    
