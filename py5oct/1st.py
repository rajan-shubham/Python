file = input("Enter the file name: ")
try:
    with open (file, 'rt') as f:
        print('Lines starting with the word From are: \n')
        count=0
        for lines in f:
            line=lines.strip()
            if line.startswith('From'):
                print(line)    
                count=count+1
        print(count)        
except:
    print("File cannot be opened.")    
