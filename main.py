from alphabet import alphabet, numbers, morse_code_alph, morse_code_nums


def to_morse_code(string):
    for char in string:
        if char in alphabet:
            position = alphabet.index(char)
            string = string.replace(char, morse_code_alph[position] + ' ')
        elif char in numbers:
            position = numbers.index(char)
            string = string.replace(char, morse_code_nums[position] + ' ')

    print(string)


def to_alphabet(string):
    for char in string:
        if char in morse_code_alph:
            position = morse_code_alph.index(char)
            string = string.replace(char, alphabet[position] + ' ')
        elif char in morse_code_nums:
            position = morse_code_nums.index(char)
            string = string.replace(char, numbers[position] + ' ')

    print(string)


print('Welcome to the Morse Code Generator!')
direction = input("Type 'encode' to convert to Morse Code, type 'decode' to convert to English Alphabet:\n").lower()


message = input("What is your message?\n").lower().replace(" ", "   ")
print(message)
