import random
import string

def generate_random_numbers(length):
    numbers = [random.randint(1, 100) for _ in range(length)]
    numbers.sort()  # Sort the numbers in ascending order
    return ' '.join(map(str, numbers))


def create_test_file(filename, num_test_cases):
    with open(filename, 'w') as file:
        file.write(f"{num_test_cases}\n")
        
        for _ in range(num_test_cases):
            n = random.randint(1, 10)
            file.write(f"{n}\n")
            str1 = generate_random_numbers(n)
            file.write(f"{str1}\n")

# Specify the number of test cases and the filename
num_test_cases = 10000  # You can change this number
create_test_file("input.txt", num_test_cases)
