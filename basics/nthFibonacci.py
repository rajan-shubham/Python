import math

def fibonacci_nth(n):
    # Golden ratio
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    # Binet's formula for the nth Fibonacci number
    fib_n = (phi**n - psi**n) / math.sqrt(5)
    
    # Since the result can have floating point precision issues, round it
    return round(fib_n)

# Example: Find the 10th Fibonacci number
print("Enter nth num for Fibonacci : ", end="")
n = int(input())
print(f"The {n}th Fibonacci number is {fibonacci_nth(n)}")
