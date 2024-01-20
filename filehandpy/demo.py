# read()
# readline()
# readlines()
f = open("data.txt",mode='r')
# print(list(f)) -> ['hello\n', 'world\n', 'bye']
for line in f:
    print(line,end="")
f.close()


#Q> How many lines a file contains ?
print()
f = open("data.txt",mode='r')
line_count = 0
for line in f:
    line.split()
    line_count += 1
print(f"Number of lines are : {line_count}")
f.close()


#Q> where the pointer is of finding the position of pointer? (0 based indexing)
f = open("data.txt",mode="r")
print(f.tell()) #0
f.read(3)
print(f.tell()) #3
f.read()
print(f.tell()) #15
f.close()



# seek() method is used to change the position of file pointer, also pointer position is always counted from the begining.

f = open("data.txt", mode="r")
print(f.tell())
print(f.read(3))
f.seek(0)
print(f.read())
f.close()