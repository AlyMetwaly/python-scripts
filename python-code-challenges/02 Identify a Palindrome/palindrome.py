import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    print(forwards)
    backwards = forwards[::-1]
    print(backwards)
    return forwards == backwards

if __name__ == '__main__':
    print(is_palindrome('hello world'))
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))