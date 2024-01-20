f = open("data1.txt", mode="r")
number_of_words = 0
number_of_chars = 0
number_of_lines = 0
for line in f:
    number_of_lines += 1
    line = line.strip("\n")
    number_of_chars += len(line)
    list1 = line.split()
    number_of_words += len(list1)
print(f"num of lines {number_of_lines} , num of words {number_of_words} , num of charactor {number_of_chars}")
f.close()