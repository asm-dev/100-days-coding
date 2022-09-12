import random

letras = list("qwertyuiopasdfghjklzxcvbnm")
numeros = list("1234567890")
simbolos = list("!£$%^&*()_+")

saludo= "Bienvenido al generador de contraseñas\n"


print(f"\n{saludo}")
print("*" * (len(saludo) - 1))

num_letras = int(input("\n¿Cuántas letras quieres añadir? ")) #5
num_simbolos = int(input("\n¿Cuántos símbolos "))
num_numeros = int(input("\n¿Cuántos números? "))

caracteres_contrasena = []

for n in range(1, num_letras + 1): #12345 = 5 items = 5 times 
  caracteres_contrasena.append(random.choice(letras)) #append 5 letras aleatorias

for n in range(1, num_simbolos + 1): 
  caracteres_contrasena.append(random.choice(simbolos))

for n in range(1, num_numeros + 1): 
  caracteres_contrasena.append(random.choice(numeros))

random.shuffle(caracteres_contrasena)

contrasena = ""

for caracter in caracteres_contrasena:
  contrasena += caracter

print(f"\nTu contraseña es: {contrasena}")