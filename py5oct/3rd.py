file = input("Enter the file name: ")
try:
    with open (file, 'rt') as f:
        count=0
        print('Lines starting with the word From are: ')
        for lines in f:
          line=lines.strip()
          if '@uct.ac.za' in line:   
            count=count+1
        print(count)
except:
    print("File cannot be opened.")