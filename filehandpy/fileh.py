# f = open("hello.txt", mode="r")

# if f:
#     print("file successfully opened")
# print(type(f))
# print(f)
# f.close();

# f = open("hello.txt","rt")
# data = f.read()
# print(data)
# f.close

# f = open("hello.txt","rb")
# data1 = f.read()
# print(data1)
# f.close()

# in text mode open encoding happens but in binary mode encoding not happens

f = open("hello.txt",mode="r")
data = f.readline() #or data = f.readline(3 no. of char)
data1 = f.readline() #of data1 = f.readline(2 no. of char)
print(data,end="")
print(data1,end="")
f.close()