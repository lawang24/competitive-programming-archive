import sys
import collections
import math

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

def solve(n,bridges):
    # set initial times first
    fastest = [math.inf for _ in range(n)]
    fastest[0] = 0
    
    prefix = [0 for _ in range(n+1)]

    # s represents Bessie starting position
    # Elsie only has access to bridges before s
    for s in range(n):
        b = s-1
        # add alternate bridges that are now accessible
        for nei in bridges[b]:
            fastest[nei] = min(fastest[nei], fastest[b]+1)
            # time we need to beat : nei-s
            r = nei - fastest[nei] 
            if r > s:
                prefix[s]+=1
                prefix[r]-=1
                
                
    ans = [0 for _ in range(n)]
    
    for i in range(n):
        ans[i] = ans[i-1] + prefix[i]
        
    output = ["0" if ans[i] else "1" for i in range(n-1)]
     
    return "".join(output)   
                
num_tests = get_int()
final_result = []

for _ in range(num_tests):
    n, m = get_list_int()
    bridges = collections.defaultdict(list)
    # normal bridges
    for i in range(1,n):
        bridges[i-1].append(i)
    for _ in range(m):
        u, v = get_list_int()
        bridges[u-1].append(v-1)
    ans = solve(n,bridges)
    final_result.append(ans)
    

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

