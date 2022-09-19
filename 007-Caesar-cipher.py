from functions import pos_letra  
from functions import encriptador_cesar

def evalua (str, abc):
        for letra in str:
            if not letra in abc:
                return False

print(f"\nBienvenido al encriptador César\n")

abecedario = list("abcdefghijklmnñopqrstuvwxyz")

de_nuevo = True
while de_nuevo == True:

    mensaje = input("\nEscribe tu mensaje (sin espacios):\n").lower()
    encriptar = input("\nEscribe D para desencriptar, E para encriptar:\n").upper()
    valor = int(input("\nNúmero:\n"))
    
    while evalua (mensaje, abecedario) == False:
        print(f"\nAl menos uno de los caracteres introducidos no se encuentra en el abecedario. Puedes introducir mensajes que contengan los siguientes caracteres {abecedario}.\n\nPor favor introduce un mensaje válido.\n")
        mensaje = input("\nEscribe tu mensaje (sin espacios):\n").lower()
        encriptar = input("\nEscribe D para desencriptar, E para encriptar:\n").upper()
        valor = int(input("\nNúmero:\n"))
    
    nuevo_mensaje = encriptador_cesar(mensaje, encriptar, valor, abecedario)
    print(f"Tu nuevo mensaje es {nuevo_mensaje}")
        
    # TESTEO:
    # hola_enc = encriptador_cesar("hola", 5, "E", abecedario)
    # hola_des = encriptador_cesar(hola_enc, 5, "D", abecedario)
    # print(hola_enc)
    # print(hola_des)

    if input("\n¿Quieres encriptar o desencriptar otro mensaje? (S/N) ").upper() != "S":
        de_nuevo = False
