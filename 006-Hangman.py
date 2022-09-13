import random

"""  
POR HACER -- Escribir documentacion
"""   
# POR HACER -- Revisar sistema de vidas. Letras no repetidas. X Valores numericos

def comprueba_letra (palabra, letra):
    posicion = []
    for n in range(len(palabra)):
        if palabra[n] == letra:
            posicion.append(n)
    return posicion

palabras = ["casa", "manzana", "jarra", "postura"]
palabra = random.choice(palabras).upper()
espacios_blanco = "_" * len(palabra)

print(espacios_blanco)

vidas = 10

while vidas > 0:
    letra = input("Dime una letra: ").upper()
    comprobacion = comprueba_letra(palabra, letra)
    if comprobacion == []:
        print("La letra no esta")
        vidas -= 1
        print(f"Te quedan {vidas} vidas")
    else:
        for i in comprobacion:
            lista_espacios = list(espacios_blanco)
            lista_espacios[i] = letra
            espacios_blanco = ''.join(lista_espacios)
        print(espacios_blanco)    


