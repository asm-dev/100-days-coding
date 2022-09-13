import random

"""  
POR HACER -- Escribir documentacion
"""   
# POR HACER -- While vidas, sustitucion espacios en blanco por letra


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

letra = input("Dime una letra: ").upper()

comprobacion = comprueba_letra(palabra, letra)

if comprobacion == []:
    print("La letra no esta")
else:
    print(f"La letra se encuentra en las posiciones {comprobacion}")



