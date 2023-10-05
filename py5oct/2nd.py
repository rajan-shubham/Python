file = input("Enter the file name: ")
try:
    with open (file, 'rt') as f:
        print('Lines not starting with the word From are: ')
        count=0
        for lines in f:
            line=lines.strip()
            if not line.startswith('From'):       
                count=count+1
        print(count)        
except:
    print("File cannot be opened.")    
