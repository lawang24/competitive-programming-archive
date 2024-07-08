import sys

FILE = 0 # if needed change it while submitting

if not FILE:
    sys.stdin = open('milkorder.in', 'r')
    sys.stdout = open('milkorder.out', 'w')
else:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def get_list_int():
    return list(map(int,get_string().split()))

def solve(n ,m ,k, hierarchy ,fixed_positions):
    
    if 1 in fixed_positions:
        return fixed_positions[1]
    
    final_positions = [0 for _ in range(n+1)]
    final_positions[0] = n+1
    
    for cow in fixed_positions:
        final_positions[fixed_positions[cow]] = cow
  
    
    # print(final_positions)
    
    # i is the next free open position
        
    # if 1 in hierarchy check everyone to the beginning ahead of 1
    if 1 in hierarchy:
        j = 0
        i = 0
        while i<=n:
            while hierarchy[j] in fixed_positions:
                i = fixed_positions[hierarchy[j]] + 1
                j+=1
            if final_positions[i] == 0:
            # print(final_positions[i], hierarchy[j])
                if hierarchy[j] == 1:
                    return i
                j+=1
            
            i+=1
        
    # if 1 is not in the hierarchy or fixed positions chuck everyone to the back
    i = n
    hierarchy_pointer = m-1
    
    while i>=0 and hierarchy_pointer>=0:
        curr_cow = hierarchy[hierarchy_pointer]
        if curr_cow in fixed_positions:
            i = fixed_positions[curr_cow]
        final_positions[i] = curr_cow
        hierarchy_pointer-=1
        i-=1
        
    for i in range(1,n+1):
        if final_positions[i] == 0:
            return i

n, m, k = get_list_int()
fixed_positions = {}
hierarchy = get_list_int()
for _ in range(k):
    cow, position = get_list_int()
    fixed_positions[cow] = position
ans = solve(n, m, k, hierarchy, fixed_positions)
sys.stdout.write(str(ans))
