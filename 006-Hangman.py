

"""  

¿QUÉ HACE EL PROGRAMA?
**********************

Este programa emula el juego clásico del ahorcado.
Toma una palabra de la lista "palabras" aleatoria, y genera el equivalente de espacios a rellenar.
Calcula las vidas disponibles, y genera una lista vacía de letras. 
Después entra en un bucle que funciona siempre y cuando el usuario tenga vidas disponibles.
Las vidas se van agotando conforme el usuario selecciona letras que no estén en la palabra (letra y palabra se comparan con la función compara_letra). 
Si el usuario introduce la misma letra más de una vez, es decir, que ya se haya introducido previamente, se le informa y se vuelve a solicitar que introduzca una letra. 
Los espacios en blanco se van sustituyendo por las letras pertinentes.
Cuando todos los espacios en blanco se han rellenado, y por lo tando adivinado la palabra, el programa termina.


POSIBLES MEJORAS/ITERACIONES:
*****************************
!!! Evitar el uso de valores numéricos, palabras enteras, etc. cuando se solicita una letra
- Niveles de dificultad (dar opción de tener más o menos vidas)
- Mejorar la UI
- Dar la opción de jugar de nuevo, llevando un contador de palabras adivinadas (sin perder, perdiendo, etc. Hay varias opciones). Al jugar de nuevo,
evitar la repetición de palabras. Gamificación -- Premio cuando se completa.
- Generar una lista mayor de palabras. 
- Repensar si el programa podría ser mejorado con funciones, POO, etc.
- Pulir pequeños detalles, como la manera en la que se muestra la lista de letras ya usadas, el uso del singular cuando son varias letras, etc.

"""   

import random
from functions import comprueba_letra

palabras = ["casa", "manzana", "jarra", "postura", "reloj", "colores", "regocijo"]
palabra = random.choice(palabras).upper()
espacios_blanco = "_" * len(palabra)

vidas = len(palabra)*2
letras = []

print(f"Tienes {vidas} vidas. La palabra tiene {len(palabra)} letras.\n\n{espacios_blanco}\n")

while vidas > 0:
    letra = input("Dime una letra: ").upper()
    while letra in letras:
        letra = input(f"\nDime una letra que no sea {letras}, ya la has usado: ").upper()
    letras.append(letra)
    comprobacion = comprueba_letra(palabra, letra)
    if comprobacion == []:
        vidas -= 1
        print(f"\nLa letra no está en la palabra. Te quedan {vidas} vidas.\n")
    else:
        for i in comprobacion:
            lista_espacios = list(espacios_blanco)
            lista_espacios[i] = letra
            espacios_blanco = ''.join(lista_espacios)
        print(f"\n{espacios_blanco}\n")    
    if espacios_blanco == palabra:
        break

if vidas == 0:
    print("Tienes cero vidas, se termina el juego")
else:
    print("Felicidades, has adivinado la palabra")
