from alphabet import alphabet, numbers, morse_code_alph, morse_code_nums
from art import logo


def to_morse_code(string):
    for char in string:
        if char in alphabet:
            position = alphabet.index(char)
            string = string.replace(char, morse_code_alph[position] + '   ')
        elif char in numbers:
            position = numbers.index(char)
            string = string.replace(char, morse_code_nums[position] + '   ')

    print(f"The encrypted message is:\n{string}")


# def to_alphabet(msg):
#     for word in msg:
#         for char in word:
#             if char in morse_code_alph:
#                 position = morse_code_alph.index(char)
#                 msg = msg.replace(char, alphabet[position])
#             elif char in morse_code_nums:
#                 position = morse_code_nums.index(char)
#                 msg = msg.replace(char, numbers[position])
#
#     print(msg)

print(logo)
print('Welcome to the Morse Code Generator!')

done = False
while not done:
    message = input("What is your message?\n").lower().replace(" ", "       ")
    to_morse_code(message)

    restart = input("Type 'yes' if you want to convert another message. Otherwise type 'no'.\n")
    if restart == "no":
        done = True
        print("Thanks for using the Morse Code Generator!")
