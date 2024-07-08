import sys
from os import path

FILE = False # if needed change it while submitting

if FILE:
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

def get_int():
    return int(sys.stdin.readline())

def get_string():
    return sys.stdin.readline().strip()

def createString(length):
    if length == 1:
        return ""
    
    if length%2 == 1:
        string="ABAA"
    else:
        string = "AA"
        
    AA = False
    for _ in range(1,length//2):
        if AA:
            string+="AA"
        else:
            string+="BB"
        AA = not AA
    
    return string

def build_special_string(count):
    """
    Build a string of uppercase Latin letters with exactly n special characters.
    A character is special if it is equal to exactly one of its neighbors.
    """
    
    if count == 1:
        return ""
    # Start with a base string that will guarantee the first special character.
    base_string = "AB"  # This will have no special characters initially.
    special_chars_needed = count
    # Add pairs of characters to ensure we get the required number of special characters.
    while special_chars_needed > 0:
        if special_chars_needed % 2 == 0:  # If even number of specials needed, add "AA" or "BB"
            if base_string[-1] == "B":
                base_string += "AA"
            else:
                base_string += "BB"
            special_chars_needed -= 2  # Two special characters added.
        else:  # For odd, just add one more to make it even (preparation step).
            base_string += "B" if base_string[-1] == "A" else "A"
            special_chars_needed -= 1
            
    return base_string

    
n = get_int()

final_result = []
for i in range(n):
    t = get_int()
    ans = build_special_string(t)
    if len(ans):
        final_result.append("YES")
        final_result.append(ans)
    else:
        final_result.append("NO")
          

for item in final_result:
    sys.stdout.write(item)
    sys.stdout.write('\n')

