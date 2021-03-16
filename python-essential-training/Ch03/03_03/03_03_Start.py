# Files and File Writing

# Open a file
my_file = open("scores.txt", "w")
# w --> write
# r --> read
# r+ --> read and write
# a --> append
# Show attributes and properties of that file
print("Name " + my_file.name)
print("Name " + my_file.mode)
# Write to a file
my_file.write("GBJ : 100\nKHD :99\nBBB : 89")
my_file.close()
# Read the file
my_file2 = open("scores.txt", "r")
print("Reading...\n" + my_file2.read(10))
my_file2.seek(0)
print("Reading again\n" + my_file2.read(10))
