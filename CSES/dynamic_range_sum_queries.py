import sys

FILE = 0 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def update(idx, new):
    pos = idx + n
    tree[pos] = new
    pos //= 2
    while pos >= 1:
        tree[pos] = tree[pos*2] + tree[pos*2+1]
        pos//=2
    
def query(l, r):
    ans = 0
    lpos, rpos = l+n, r+n
    while lpos<=rpos:
        # if lidx right child, add and dip
        if lpos % 2 :
            ans += tree[lpos]
            lpos+=1
        # if ridx is left child:
        if not rpos % 2:
            ans+=tree[rpos]
            rpos-=1
        lpos//= 2
        rpos//=2
        
    return ans
            
n, q = get_list_int()
tree = [0 for _ in range(2*n)]
nums = get_list_int()
for i in range(n):
    tree[-1-i] = nums[-1-i]
for i in range(n-1, 0, -1):
    tree[i] = tree[i*2] + tree[i*2+1]
    
for _ in range(q):
    command, n1, n2 = get_list_int()
    if command == 1:
        update(n1-1, n2)
    else:
        print(query(n1-1, n2-1))