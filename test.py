import random
import string

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def create_test_file(filename, num_test_cases):
    with open(filename, 'w') as file:
        file.write(f"{num_test_cases}\n")
        
        for _ in range(num_test_cases):
            n = random.randint(1, 100)
            file.write(f"{n} 3\n")
            
            str1 = generate_random_string(n)
            str2 = generate_random_string(n)
            
            file.write(f"{str1}\n{str2}\n")

# Specify the number of test cases and the filename
num_test_cases = 10000  # You can change this number
create_test_file("test.txt", num_test_cases)
