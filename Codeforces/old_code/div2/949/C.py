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

def arr_to_str(arr):
    return " ".join(str(x) for x in arr)

def getPath(v1, v2):

    left = []
    right = []

    while v1!=v2:
        if v1>v2:
            left.append(v1)
            v1>>=1
        else:
            right.append(v2)
            v2>>=1
    
    left.append(v1)
    left.extend(reversed(right))
        
    return left


def find_connectors(v1, v2, length):

    full_path = getPath(v1, v2)

    if len(full_path)%2 != length%2 or len(full_path) > length:
        return -1
    
    s2 = full_path[-1]

    s1 = full_path[-2] if len(full_path) >1 else s2 * 2

    while len(full_path) < length:
        full_path.append(s1)
        full_path.append(s2)

    return full_path[1:-1]
    
# class Node:
#     def __init__(self,val,left,right) -> None:
#         self.val = val
#         self.left = left
#         self.right = right
    
    
# def build_graph(val, maximum):
#     if val > maximum:
#         return None
    
#     left = build_graph(val*2, maximum)
#     right = build_graph(val*2+1, maximum)
    
#     this_node = Node(val, left, right)
    
#     return this_node
    

def solve(n, nums):
    
    maximum = max(nums)
    if maximum == -1:
        return arr_to_str([x%2+1 for x in range(len(nums))])
    
    ans = nums[:]
    
    # graph = build_graph(1, maximum)
    i = 0
    
    while i<n and nums[i]==-1:
        i+=1
        
    # handle start of array
    for k in range(i):
        if k%2==0:
            ans[i-k-1] = ans[i-k] * 2
        else:
            ans[i-k-1] = ans[i-k] // 2

    j = i+1
    while j<n:
        if nums[j]!=-1:
            arr = find_connectors(nums[i],nums[j], j-i+1)
            if arr == -1:
                return "-1"
            for k in range(len(arr)):
                ans[j-1-k] = arr[-(k+1)]
            i = j
        j+=1

    # handle end of array
    for j in range(n-1-i):
        if j%2==0:
            ans[i+j+1] = ans[i+j] * 2
        else:
            ans[i+j+1] = ans[i+j] // 2
    
    return arr_to_str(ans)
    

t = get_int()

final_result = []

for _ in range(t):
    n = get_int()
    nums = get_list_int()
    ans = solve(n, nums)
    final_result.append(str(ans))

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

