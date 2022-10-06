import random

def char_entry(char_type):
  return int(input(f"\nHow many {char_type} would you like to add? "))

def random_char(accum, num_char, char_list):
  for n in range (0, num_char): 
    accum.append(random.choice(char_list))
  return accum

letters = list("qwertyuiopasdfghjklzxcvbnm")
nums = list("1234567890")
syms = list("!£$%^&*()_+")

saludo= "Welcome to your password generator\n"

print(f"\n{saludo}")
print("*" * (len(saludo) - 1))

num_letters = char_entry("letters")
num_syms = char_entry("symbols")
num_nums = char_entry("numbers")

password_list = []

random_letters = random_char(password_list, num_letters, letters)
random_numbers = random_char(password_list, num_nums, nums)
random_symbols = random_char(password_list, num_syms, syms)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"\nTu contraseña es: {password}")
print(len(password))