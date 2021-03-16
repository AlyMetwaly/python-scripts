# Iterative Files
myFile = open("scores.txt", "r")

# Read one line at a time
print("My one line is " + myFile.readline())
myFile.seek(0)

# Iterate through each line of a file
for line in myFile:
    new_higher_score = line.replace("BBB", "PDJ")
    print(new_higher_score)

myFile.close()
