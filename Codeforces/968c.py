import sys
import collections
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

def solve(n, _string):
    count = collections.Counter(_string)
    heap = [(-x[1],x[0]) for x in count.most_common()]
    heapq.heapify(heap)
    ans = []
    
    while heap:
        number, letter = heapq.heappop(heap)
        ans.append(letter)
        number+=1
        if number:
            heapq.heappush(heap, (number, letter))
    
    return "".join(ans)
        
final_result = []

t = get_int()

for _ in range(t):
    n = get_int()
    _string = get_string()
    answer = solve(n, _string)
    final_result.append(answer)

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

