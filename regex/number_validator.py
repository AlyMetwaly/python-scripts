import re
#your code goes here
str = input()
pattern = r"^[189][0-9]{7}$"
match = re.search(pattern, str)
if match:
    print("Valid")
else:
    print("Invalid")