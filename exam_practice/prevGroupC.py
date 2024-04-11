# Q5.A> what is _init_ in Python?
#`__init__` (often pronounced "dunder init") is a special method in Python classes used for initializing new instances of the class. It's called the constructor method because it initializes the object. 

#When you create a new instance of a class, Python automatically calls the `__init__` method for that class. This method is where you typically initialize instance variables and perform any setup that's necessary for the object to function properly.

#Here's a simple example to illustrate how `__init__` works:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes of the person object
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30

#In this example, the `__init__` method initializes two instance variables, `name` and `age`, with the values provided when creating a new `Person` object (`person1`).
# Q 5.A(ii) Write down the differences between break,continue, and pass. in python
# break:
#break is used inside loops (like for or while) to exit the loop prematurely.
#When break is encountered, the loop is immediately terminated, and the program execution continues with the next statement after the loop.
#It's often used when a certain condition is met, and you want to exit the loop early.

#continue:
#continue is also used inside loops (like for or while).
#When continue is encountered, the current iteration of the loop is stopped, and the loop proceeds with the next iteration.
#It's useful when you want to skip some part of the loop's code for certain iterations based on a condition.

#pass:
#pass is a no-operation statement in Python.
#It is used when a statement is syntactically required but you do not want to execute any code.
#It's often used as a placeholder when writing code that will be implemented later.
#Unlike break and continue, pass does not affect the flow of control in loops; it simply does nothing.


# Q 5.A(iii) What is the purpose of is, not and in operators?
# The `is`, `not`, and `in` operators are used in Python for different purposes:

# 1. `is` Operator:
#    - The `is` operator checks whether two variables refer to the same object in memory.
#    - It returns `True` if the operands refer to the same object, and `False` otherwise.
#    - It does not compare the values of the objects; it only compares their identities.

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(x is y)  # Output: False (Different objects)
print(x is z)  # Output: True (Same object)

# 2. `not` Operator:
#    - The `not` operator is a logical negation operator.
#    - It reverses the logical value of a boolean expression. If the expression is `True`, `not` makes it `False`, and vice versa.

a = True
b = False

print(not a)  # Output: False
print(not b)  # Output: True

# 3. `in` Operator:
#    - The `in` operator checks for membership in sequences (lists, tuples, strings, etc.) or mappings (dictionaries).
#    - It returns `True` if a value exists within the sequence or mapping, and `False` otherwise.


my_list = [1, 2, 3, 4, 5]

print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

my_string = "Hello, World!"

print("o" in my_string)  # Output: True
print("z" in my_string)  # Output: False

# These operators are fundamental in Python and are frequently used in conditional statements, loops, and other control flow constructs to make decisions based on certain conditions or to check for the presence of elements within data structures.

# Q 5.A (iv) python prog for pattern.
# 1
# 22
# 333
# 4444
# 55555
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i, end='')
    print()

# OR 5.B(i) How can the ternary operator be used in python ?
# In Python, the ternary operator allows you to write conditional expressions in a compact form. The syntax for the ternary operator is:
x = 5
y = 10

result = x if x > y else y
print(result)  # Output: 10

# Q 5.B(ii)write down the key feature of Python .
# Python is a versatile programming language with several key features that contribute to its popularity and effectiveness for various purposes. Here are some of the key features of Python:

# 1. **Simple and Easy to Learn:** Python has a clean and simple syntax that emphasizes readability and reduces the cost of program maintenance. This makes it an ideal language for beginners as well as experienced programmers.

# 2. **Interpreted and Interactive:** Python is an interpreted language, which means that code can be executed directly without the need for compilation. Additionally, Python supports an interactive mode that allows for quick experimentation and testing of code snippets.

# 3. **High-level Language:** Python abstracts away low-level details such as memory management and provides high-level data structures, making it easier to focus on solving problems rather than managing the complexities of the computer.

# 4. **Dynamic Typing:** Python uses dynamic typing, which means that variable types are determined at runtime. This allows for flexible and expressive code but requires careful attention to variable types to avoid potential issues.

# 5. **Cross-platform:** Python is available on various platforms, including Windows, macOS, and Linux, making it a portable language that can be used for developing applications across different operating systems without modification.

# 6. **Rich Standard Library:** Python comes with a comprehensive standard library that provides support for a wide range of tasks, from file I/O to networking to web development. This reduces the need to rely on third-party libraries for many common programming tasks.

# 7. **Large Ecosystem of Third-party Libraries:** In addition to the standard library, Python has a vast ecosystem of third-party libraries and frameworks that extend its functionality for specific domains such as data science, web development, and machine learning. Popular libraries include NumPy, pandas, Django, Flask, TensorFlow, and PyTorch.

# 8. **Community Support:** Python has a large and active community of developers who contribute to its development, create tutorials and documentation, and provide support through forums, mailing lists, and online communities. This community-driven approach fosters collaboration and innovation within the Python ecosystem.

# 9. **Open-source:** Python is an open-source language, meaning that its source code is freely available for anyone to view, modify, and distribute. This encourages transparency, collaboration, and continuous improvement of the language.

# 10. **Versatility:** Python is a multipurpose language suitable for a wide range of applications, including web development, desktop GUI applications, scientific computing, data analysis, artificial intelligence, automation, and more. Its versatility makes it a popular choice for developers working in various fields.

# Q 5.B(iii) What is the difference between / and // operator in python ?
# / (Regular Division):
# The / operator performs regular division and returns a floating-point result.
# It divides the left operand by the right operand and returns the quotient as a floating-point number, regardless of whether the operands are integers or floats.
result = 10 / 3
print(result)  # Output: 3.3333333333333335

# // (Floor Division):
# The // operator performs floor division and returns the largest integer that is less than or equal to the quotient.
# It divides the left operand by the right operand and returns the integer part of the quotient

result = 10 // 3
print(result)  # Output: 3

# 5.B(iv)Write a python program for the following pattern.
# 1
# 2 3
# 4 5 6
# 7 8 9 IO
# 11 12 13 14 15

rows = 5
num = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()
