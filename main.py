# def greet(user_name, user_location):
#     print(f"Hello {user_name}")
#     print(f"How's the weather in {user_location}?")
#
#
# name = input("Give me your name\n")
# location = input("Where you from?\n")
# greet(name, location)

# one can covers 5m2
# (width*height)/5
# def encode(word_to_encode, step):
#     encoded = word_to_encode[::step]
#     print(encoded)
#
#
# word = input("Type word to encode\n")
# encode(word, -1)
# import math
#
#
# def count_cans(width, height, coverage):
#     m2 = width * height
#     result = math.ceil(m2 / coverage)
#     if result < 1:
#         print(f"You need {result} cans")
#     else:
#         print(f"You need {result} can")
#
#
# wall_width = float(input("Put width of the wall\n"))
# wall_height = float(input("Put height of the wall\n"))
# can = float(input("How many m2 one can of pain can cover?\n"))
#
# count_cans(wall_width, wall_height, can)

######################################################################
# prime number checker:


# def check(num_to_check):
#     # check if is divisible by other numbers
#     is_prime = True
#     for check_num in range(2, num_to_check):
#         if (num_to_check % check_num) == 0:
#             is_prime = False
#             if not is_prime:
#                 break
#     if is_prime:
#         print(f"{num_to_check} is a prime number")
#     else:
#         print("Is not a Prime number")
#
#
# user_check = int(input("Type a number to check: \n"))
# check(user_check)


######################################################################
from logo import logo
print(logo)
end = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text_to_encrypt, step):
    global message
    if shift > len(alphabet):
        step = int(input("Type valid number from 1 to 26:"))
    for char in text_to_encrypt:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + step
            message += alphabet[new_position]
        else:
            message += char


while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    message = ""

    if direction == "encode":
        caesar(text, shift)
    elif direction == "decode":
        caesar(text, (-shift))
    else:
        print("Wrong input")
        close()
    print(f"the {direction}d text is {message}\n")
    print("Want to do some more translations?")
    restart = input("yes/no\n").lower()
    if restart == "no" or restart == "":
        end = True
        print("Goodbye")
