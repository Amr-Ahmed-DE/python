#!/usr/bin/python3

#Task2: Write a Python program to test whether a passed letter is a vowel or not.

vowelLetters = ['a', 'A', 'e', 'E', 'o', 'O', 'u', 'U', 'i', 'I']

inputletter = input("pleaser enter a letter to check: ")

if inputletter in vowelLetters:
    print(f"the letter '{inputletter}' is a vowel")
else:
    print(f"the letter '{inputletter}' is not a vowel")       



