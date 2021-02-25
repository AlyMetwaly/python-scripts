import re

def palindrome(phrase):
  #find only aplhabetical characters and convert them to lower
  forwards = re.findall(r'[a-z]+',phrase.lower())
  #reverse the list
  backwards = forwards[::-1]
  return forwards==backwards

if __name__ == '__main__':
  print(palindrome("hello world"))
  print(palindrome("Go hang a salami, I'm a lasagna hog."))