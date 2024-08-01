# text = input("input >>>")

# vowels = ("a","o","e","i")
# count = 0

# for i in text:
#     if i in vowels:
#         count += 1
#     print(count)


# number = [1,2,3,3,34455,66,6,-8,99,4656]
# # find max element
# maxvalue = number[0]

# for num in number:
#     if num > maxvalue:
#         maxvalue = num

# print("Max value is", maxvalue)

import random

number = random.randint(0,100)

guess = int(input("Input quess >>>"))

while guess != number:
    if guess < number:
        print(guess, " is too low")
    elif guess > number:
        print(guess, " is a big")
    guess = int(input("Input quess >>>"))
    
print("Won")