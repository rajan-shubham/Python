# name = input("What is your name ? ")
# print("hello, name")

#name = input("What is your name ? ")
# print("hello, ")
# print(name)

# print("hello,"+name)
# print("hello, ",name)

# print("hello, "+name)
# print("hello,",name)

# print('hello, "friend"')
# print("hello, \"friend\"")

#print(f"hello, {name}")
#here the f is formet specifier

#name = input("What is your name ? ")
#name = name.strip()
#name = name.capitalize()
#name = name.title()


name = input("what's your name ? ").strip().title()
first,last = name.split()
print(f"hello, {name}")

# x = input("Give a no. x : ")
# y = input("Give a no. y : ")
# print(x+y)

# x = int(input("Give a no. x : "))
# y = int(input("Give a no. y : "))
# print(x+y)

#round(number [ ,ndigits=])

# x = float(input("Give a no. x : "))
# y = float(input("Give a no. y : "))
# z = round(x+y)
# print(z)

x = float(input("Give a no. x : "))
y = float(input("Give a no. y : "))
#z = x + y
#print(f"{z}")
#print(f"{z:,}")

# z = round(x/y,3)
# print(z)

z = x/y
print(f"{z:.2f}")

#extra thing that i get
# print("hello","ji",sep=" ")
# hello ji

# In [7]: print("hello","ji")
# hello ji

# In [8]: print("hello","ji",sep="@ ")
# hello@ ji

# In [9]: print("hello","ji",sep="@")
# hello@ji


# print("hello","ji",end='\n')
# hello ji

# In [15]: print("hello","ji",end='\n\n\n')
# hello ji



# In [16]: print("hello","ji",end='1\n2\n3\n')
# hello ji1
# 2
# 3
