import random
import string

import random

def generate_random_tree_edges(n):
    if n <= 1:
        raise ValueError("A tree must have at least 2 nodes.")

    # Start with the first node
    nodes = [1]  # Tree starts with node 1
    edges = []

    # Add remaining nodes
    for new_node in range(2, n + 1):
        # Randomly select an existing node to connect to the new node
        existing_node = random.choice(nodes)
        edges.append((existing_node, new_node))
        nodes.append(new_node)

    return edges



def create_test_file(filename, num_test_cases):
    with open(filename, 'w') as file:
        file.write(f"{num_test_cases}\n")
        
        for _ in range(num_test_cases):
            n = random.randint(2, 10)
            file.write(f"{n}\n")
            for _ in range(n):
                l = random.randint(1, 100)  # Adjust range as needed
                r = random.randint(l + 1, 200)  # Ensure r > l by starting from l + 1
                file.write(f"{l} {r}\n")
            edges = generate_random_tree_edges(n)
            for u, v in edges:
                file.write(f"{u} {v}\n")

# Specify the number of test cases and the filename
num_test_cases = 1000000  # You can change this number
create_test_file("input.txt", num_test_cases)
