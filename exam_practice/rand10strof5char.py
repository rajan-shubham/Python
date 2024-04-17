# Generate list of 10 randomly generated 5 character strings
import random
import string
random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)]

# Print the list
print(random_strings)

# Write Python code to print a list of 10 randomly generated 5 character strings. Your code Must use list comprehension. you may use the 'choice' function from the 'random' python library.
def string_lengths(input_list):
    return [len(string) for string in input_list]

# Example usage:
input_strings = ["hello", "world", "python", "list", "comprehension"]
result_lengths = string_lengths(input_strings)
print(result_lengths)