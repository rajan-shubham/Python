# Q2.A>
# Write Python code to print a list of 10 randomly generated 5 character strings. Your code Must use list comprehension. you may use the 'choice' function from the 'random' python library.
import random
import string

# Generate list of 10 randomly generated 5 character strings
random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)]

# Print the list
print(random_strings)

# 2nd WAY WITHOUT USING IMPORT STRING
import random

# Generate list of 10 randomly generated 5 character strings
random_strings = [''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5)) for _ in range(10)]

# Print the list
print(random_strings)


# Q2.B>
# Write Python code to print a list of 10 randomly generated 5 character strings. Your code Must use list comprehension. you may use the 'choice' function from the 'random' python library.
def string_lengths(input_list):
    return [len(string) for string in input_list]

# Example usage:
input_strings = ["hello", "world", "python", "list", "comprehension"]
result_lengths = string_lengths(input_strings)
print(result_lengths)



# Q3.A>
# Write a Python function that takes a string and returns a string containing only the vowels in the input string. For example, if the input string to your function is "hello", then the output string from this function should be "eo".
def extract_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in input_string if char in vowels)

# Example usage:
input_string = "shubham rajan"
output_string = extract_vowels(input_string)
print(output_string)  # Output: "uaaa"


# Q3.B>
# Write a Python function that takes a string and returns an integer representing the number of consonants in the input string. For example, if the input string is "hello", then the output from your function should be 3 (since there are 3 consonants).
def count_consonants(input_string):
    vowels = 'aeiouAEIOU'
    return len([char for char in input_string if char.isalpha() and char not in vowels])

# Example usage:
input_string = "hello"
consonant_count = count_consonants(input_string)
print(consonant_count)  # Output: 3


# Q4.A>
# Write Python code to print a list of 10 randomly generated 5 character strings. Your code Must use list comprehension. you may use the 'choice' function from the 'random' python library.

# Write 5 test cases for the function in above. Make sure that the test cases run ONLY if the program file is run directly using Python, but NOT if the file is imported as a module in another Python program.
import random
import string

def generate_random_strings():
    return [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)]

# Test cases
def test_generate_random_strings():
    generated_strings = generate_random_strings()
    assert len(generated_strings) == 10
    for string in generated_strings:
        assert len(string) == 5
        assert all(c.isalnum() for c in string)

if __name__ == "__main__":
    test_generate_random_strings()
    print("All tests passed.")
