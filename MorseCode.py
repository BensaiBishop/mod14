"""

Name:Benjamin Bishop
Date:22 Aug 2021
Assignment:Assignment #1
Due Date:(Due Date)
About this project: This project is an simple introductory exercise with python.
Assumptions: User should be able to input a valid string and have the appropriate morse translation output.
All work below was performed by Benjamin Bishop

Attached is a copy of the test run

C:\Users\bensa\PycharmProjects\pythonProject\venv\Scripts\python.exe C:/Users/bensa/PycharmProjects/pythonProject/MorseCode.py
Enter in the text.... Hello World 9
....
.
.-..
.-..
---

.--
---
.-.
.-..
-..

----.


Process finished with exit code 0

"""

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
