with open('Sample_Text.txt', 'rt') as file:
    dictionary={}
    dictionary2={}
    for data in file:
        data=data.strip()
        for s in range(len(data)):
            count=0
            percentage=0
            for i in data:
                if data[s]==i:
                    count+=1
                dictionary[data[s]]=count
                dictionary2[data[s]]= str((count*100)/len(data))+"%"
print("Occurence of Each letter:\n")
print(dictionary)
print("\nPercentage of Occurence of Each letter:\n")
print(dictionary2)