# Generate list of 10 randomly generated 5 character strings
import random
import string
random_strings = [''.join(random.choices(string.ascii_letters + string.digits, k=5)) for _ in range(10)]

# Print the list
print(random_strings)