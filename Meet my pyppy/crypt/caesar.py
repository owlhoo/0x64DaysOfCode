import os

alphabet = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 'k': 'k'
            , 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 'u': 'u',
            'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}


def decipher(ciphertext, key):
    plaintext = []

    for letter in ciphertext:
        if letter.isalpha():
            shift = ord(letter.lower()) + key
            if shift > ord('z'):
                new_letter = alphabet.get(chr(shift - 26))
            elif shift < ord('a'):
                new_letter = alphabet.get(chr(shift + 26))
            else:
                new_letter = alphabet.get(chr(shift))
        else:
            new_letter = letter

        plaintext.append(new_letter)
    return ''.join(plaintext)


def encipher(plaintext, key):
    ciphertext = []

    for letter in plaintext:
        if letter.isalpha():
            shift = ord(letter.lower()) + key
            if shift > ord('z'):
                new_letter = alphabet.get(chr(shift - 26))
            elif shift < ord('a'):
                new_letter = alphabet.get(chr(shift + 26))
            else:
                new_letter = alphabet.get(chr(shift))
        else:
            new_letter = letter

        ciphertext.append(new_letter)
    return ''.join(ciphertext)


def main():
    while True:
        os.system('clear')
        choice = (int(input('1. Encipher\n2. Decipher\n3. Exit\nEnter your choice: ')))

        if choice == 1:
            text = input('Enter your plaintext you want to encipher: ')
            key = int(input('Enter your key for enciphering: '))
            print(encipher(text, key))
            input()

        elif choice == 2:
            text = input('Enter your ciphertext you want to decipher: ')
            key = int(input('Enter your key for deciphering [0 for brute-force]: '))

            if key != 0:
                print(decipher(text, -key))
            else:
                for i in range(0, 26):
                    print(decipher(text, -i))
            input()

        else:
            break




if __name__ == '__main__':
        main()
