f1 = open("first.txt",mode='r',encoding="utf-8")
f2 = open("second.txt",mode="w",encoding="utf-8")
# print(f1.readlines) -> ['welcome to\n', "shubham's youtube\n", 'channel and\n', 'learn with no cost']
datalist = f1.readlines()
for line in datalist:
    f2.write(line)
f1.close()
f2.close()