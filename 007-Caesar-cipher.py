from functions import pos_letra  
from functions import encriptador_cesar

print(f"\nBienvenido al encriptador César\n")

de_nuevo = True
while de_nuevo == True:

    mensaje = input("\nEscribe tu mensaje (sin espacios):\n").lower()
    encriptar = input("\nEscribe D para desencriptar, E para encriptar:\n").upper()
    valor = int(input("\nNúmero:\n"))
    abecedario = list("abcdefghijklmnñopqrstuvwxyz")

    # TESTEO:
    # hola_enc = encriptador_cesar("hola", 5, "E", abecedario)
    # hola_des = encriptador_cesar(hola_enc, 5, "D", abecedario)
    # print(hola_enc)
    # print(hola_des)

    nuevo_mensaje = encriptador_cesar(mensaje, encriptar, valor, abecedario)
    print(f"Tu nuevo mensaje es {nuevo_mensaje}")

    if input("¿Quieres encriptar o desencriptar otro mensaje? (S/N) ").upper() != "S":
        de_nuevo = False

## A solucionar/mejorar -- error con caracteres que no esten en el abc como "#" usando la lista abecedario
