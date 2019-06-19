"""Exercises for chapter 11"""

import sys, re

# Question 1, Reads a file and creates a dictionary. Will then output the dictionary
"""
d = {}

with open("input.txt", "r") as line:

    for word in line:
        key = ""
        value = 0

        key_from_string = re.findall('[A-Za-z]+', word)
        value_from_string = re.findall('\d+', word)

        length_of_food_name = len(key_from_string)

        if length_of_food_name > 1:
            count = 0
            while length_of_food_name > count:
                key += key_from_string[count]+" "
                count += 1
        else:
            key = key_from_string[0]

        for val in value_from_string:
            value = val

        d[key] = value

for k, v in d.items():
    print("%s : %s" % (k, v))
"""

# Question 2, Reads a file with contact details: Name, Number and Email.
# Asks a user for input. If the user exists will output the details. If not will output "No contact with that name"
"""
contact_details = {}

with open("input.txt", "r") as contact:

    for detail in contact:
        dict_input = detail.strip().split(' ')
        contact_details[dict_input[0]] = dict_input[1]+" "+dict_input[2]

input_list = []

new_user = True

while new_user is True:
    input_list.append(input("Search for a user:"))
    print("Search for another user? (Y,N)")
    yes_or_no = input().lower()
    if yes_or_no == "y":
        continue
    else:
        new_user = False

for name in input_list:
    if name in contact_details:
        phone_and_email = contact_details[name].split(' ')
        print("Name: %s \nEmail: %s \nPhone: %s \n" % (name, phone_and_email[1], phone_and_email[0]))
    else:
        print("No contact with that name\n")
"""

# Question 3, Reads input and and counts how mnay times each word appears in the text

"""Come back to this after the strings chapter!!!"""

lines = sys.stdin.readlines()
word_count_dict = {}

for line in lines:
    for word in line.strip().split(' '):
        lowercase_word = word.lower()
        if lowercase_word in word_count_dict:
            count = word_count_dict[lowercase_word]
            count += 1
            word_count_dict[lowercase_word] = count
        else:
            word_count_dict[lowercase_word] = 1
    lines = sys.stdin.readlines()

for k,v in word_count_dict.items():
    print("%s : %s" % (k,v))
