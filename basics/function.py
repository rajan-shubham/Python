# def hello():
#     print("hello")

# name = input("what's your name ? ")
# hello()
# print(name)

# def hello(to = "world"):
#     print("hello, ",to)

# hello()
# name = input("what's your name ? ")
# hello()
# hello(name)


# def main():
#     name = input("What's your name ? ")
#     hello()

# def hello():
#     print("hello, ",name)

# main()

# def main():
#     name = input("What's your name ? ")
#     hello(name)

# def hello(to = "world"):
#     print("hello, ",to)

# main()


def main():
    x = int(input("What's x ? "))
    print(x ,"Squared is :",square(x))

def square(x):
    #return x*x
    #return x**2
    return pow(x,2)

main()