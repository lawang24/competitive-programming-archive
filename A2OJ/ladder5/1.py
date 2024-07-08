import sys

FILE =  1 # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n, t, queue):
    positions = list(queue)
  
    for _ in range(t):
        i = 0
        while i<n-1:
            if positions[i] == "B" and positions[i+1] == "G":
                positions[i], positions[i+1] = positions[i+1], positions[i]
                i+=2
            else:
                i+=1    
    
    return "".join(positions)
        
final_result = []

n, t = get_list_int()
queue = get_string()
ans = solve(n, t, queue)
final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

