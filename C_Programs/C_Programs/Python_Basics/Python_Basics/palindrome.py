# Palindrome Checker in Python

def is_palindrome(text):
    return text == text[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
