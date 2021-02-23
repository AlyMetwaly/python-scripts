file = open("/usercode/files/books.txt", "r")

#your code goes here
i=1
Lines = file.readlines()
for line in Lines:
    if i < len(Lines): 
        initial = line[0]
        length = len(line)-1
        print(initial+str(length))
    else:
        initial = line[0]
        length = len(line)
        print(initial+str(length))
    i=i+1

file.close()



#for line in Lines[0:len(Lines)-1]:
#    initial = line[0]
#    length = len(line)-1
#    print(initial+str(length))