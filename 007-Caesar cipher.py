from functions import caesar_cipher

def letters_in_abc (word, abc):
        for char in word:
            if not char in abc:
                return False

print("\nWelcome to Caesar Cipher\n")

abc = list("abcdefghijklmnñopqrstuvwxyz")

again = True
while again == True:

    message = input("\nType your messages (without whitespaces):\n").lower()
    cipher_dir = input(f'\nType C to cipher "{message}" or D to decipher it:\n').upper()
    number_pos = int(input("\nPlease add a number:\n"))
    
    while letters_in_abc(message, abc) == False:
        print(f"\nWe can't use some of the characters that you have used. You can use these characters in your message: {abc}.\n\nPlease add a submit a new message.\n")
        message = input("\nType your messages (without whitespaces):\n").lower()
        cipher_dir = input(f'\nType C to cipher "{message}" or D to decipher it:\n').upper()
        number_pos = int(input("\nPlease add a number:\n"))
    
    print(f'Your new message is "{caesar_cipher(message, cipher_dir, number_pos, abc)}"')
        
    if input("\nWould you like to cipher or decipher another message? (Y/N) ").upper() != "Y":
        again = False
