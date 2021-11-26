
# Dictionary of morse code chart; added numbers just in case

MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.',
                   'D': '-..', 'E': '.', 'F': '..-.',
                   'G': '--.', 'H': '....', 'I': '..',
                   'J': '.---', 'K': '-.-', 'L': '.-..',
                   'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.',
                   'S': '...', 'T': '-', 'U': '..-',
                   'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..', '1': '.----',
                   '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----'
                   }


# Method for encryption
def encrypt(message):
    # cipher is a blank string I will translate onto
    cipher = ''
    for letter in message:
        # if its a letter concatenate with and add newline
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + '\n'
        # if its anything else newline
        else:
            cipher += '\n'

    return cipher


def main():
    message = input("Enter in the text.... ")
    # convert message to upper for translation
    result = encrypt(message.upper())
    print(result)


if __name__ == '__main__':
    main()
