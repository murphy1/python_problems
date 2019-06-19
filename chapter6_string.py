# file for Chapter 6 of slither into python

import re

# Question 1, user input will state how many decimal places 'e' should be formatted to.

"""
e = 2.7182818284590452353602874713527

format_num = input("Enter Format Number:")
form = "{:."+format_num+"f}"

print(form.format(e))
"""

# Question 2, User will input 2 numbers and a string. The string will be sliced depending on the numbers
# If the numbers are not in the range, the message will be displayed: Cannot slice using those indices

"""
string = input("Enter a string to slice:")
num1 = int(input("First num:"))
num2 = int(input("Second num:"))

if num1 > len(string) or num2 > len(string):
    print("Cannot slice using those indices!")
else:
    sliced = string[num1:num2]
    print(sliced)
"""

# Question 3, Will grade your password depending on how strong it is. Levels are 1 -> 4 depending on if it has
# digits, lowercase letters, uppercase letters or special characters

password = input("Please enter your password:")

cap_check = re.findall('[A-Z]+', password)
lowcase_check = re.findall('[a-z]+', password)
digit_check = re.findall('[0-9]+', password)
special_char_check = re.findall('[$,@.#<>%*!]+', password)

strength = 0

if len(cap_check) > 0:
    strength += 1
else:
    pass
if len(lowcase_check) > 0:
    strength += 1
else:
    pass
if len(digit_check) > 0:
    strength += 1
else:
    pass
if len(special_char_check) > 0:
    strength += 1
else:
    pass

if strength >= 3:
    print("Strength: %d, Valid Password" % (strength))
else:
    print("Strength: %d, Invalid Password" % (strength))
