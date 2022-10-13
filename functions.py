# 006-Hangman
def letter_finder(word, letter):
    """
    This function informs us of a letter's position in a word.
    If the letter is found in the word, it returns a list with this letters indexes in the word, e.g. letter_finder("casa", "a") returns [1, 3]
    If the letter isn't in the word, this function returns an empty list []
    """
    idx = []
    for n in range(len(word)):
        if word[n] == letter:
            idx.append(n)
    return idx


# 007-Caesar cipher
def letter_idx(char, list):
    """
    This function compares a letter with the elements of a list.
    The list is iterated and each element of the list is compared with the letter.
    If any element of the list is equal to the letter, the index in the list of that element is added to the empty list.
    This function is used within the Caesar function to get the idx in the alphabet of a letter.
    It returns a list.
    """
    pos = []
    for i in list:
        if char == i:
            pos.append(list.index(i))
    return pos 


# 007-Caesar-cipher
def caesar_cipher(mes, cipher, num, abc):
    """
    This function allows us to encrypt and decrypt a message. It's an encryptor.
    Its params are the message, the number of hops in the list, the direction of the hops (+/R to encrypt, -/LEFT to decrypt), and a list of values ​​(usually an alphabet)
    The inner function is explained with comments and there are also a couple of commented impressions that can be used to understand the function of this function.
    It internally uses the pos_letter function.
    """
    if cipher != "D" and cipher != "C":
        print("\nThe param cipher should be either D, to decipher, or C, to cipher\n")
        return
    elif cipher == "D":
        num = -num 

    print(f"\nYour message is {mes}, and we're going to encrypt it using a value of {num}\n")
 
    mes_list = list(mes) 
    new_mes_list = []

    for char in mes_list: 

        char_position = letter_idx(char, abc) 
        new_char_position = char_position[0] + num 

        if new_char_position > len(abc):
            new_char_position = new_char_position - len(abc)
        new_char = abc[new_char_position]

        new_mes_list.append(new_char)
        new_message = ''.join(new_mes_list)

    return new_message
        
# 008-Blind-auction
def add_bid(dict):
    """
    Allows us to add a new keyvalue pair to a dictionary
    """
    bidder = input("Name: ")
    bid = input("Bid: ")
    dict[bidder] = bid
    return dict

# 009-Calculator
def input_natural_o_cero(question="Please introduce a number bigger or equal to 0: "):
    """
    Gets an input making sure that its a number >= 0. It avoids empty imputs, letters and nums <0
    """
    num = input(question)
    if num[0] == "+":
        num = num[1:]
    while len(num) == 0 or num.isnumeric() == False or float(num) < 0:
        print("Necesitas introducir un número igual o mayor que cero")
        num = input(question)
    return float(num)