f = open("listcopy.txt",mode='w')
lines_list = ['yogesh\n','ram\n','raj\n','shantanu\n','shubham']
f.writelines(lines_list)
#f.write(lines_list)

f.close()