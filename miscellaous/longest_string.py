txt = input()
a = txt.split()
longest_string = max(a, key=len)
print(longest_string)
