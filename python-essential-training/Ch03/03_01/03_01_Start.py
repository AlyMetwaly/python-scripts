# Command Line Arguments
import sys
# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments", sys.argv)
# Remove Arguments
sys.argv.remove(sys.argv[0])
print("Arguments", sys.argv)
# Sum up the Arguments
arguments = sys.argv

sum = 0
for arg in arguments:
    try:
        sum = sum + int(arg)
    except:
        print("Bad input")

print(sum)
