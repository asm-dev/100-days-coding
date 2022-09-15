# encriptar = input("Escribe D para desencriptar, E para encriptar:\n")
# #Mensaje, sin espacios
# mensaje = input("Escribe tu mensaje (sin espacios): ").lower()
# #Pedir num
# num = input("Número: ")

def pos_letra (letra, lista):
    posiciones = []
    for i in lista:
        if letra == i:
            posiciones.append(abecedario.index(i))
    return posiciones
    
abecedario = list("abcdefghijklmnñopqrstuvwxyz")

def encriptador_cesar (mensaje, num, encriptar):
    print(mensaje)
    print(num)  
    nuevo_mensaje = []
    if encriptar == "D":
        num = -num 
    lista_mensaje = list(mensaje)
    for letra in lista_mensaje:
        posicion_letra = pos_letra(letra, abecedario) #cada letra del abecedario, compara letra que damos con ella, si coincide, nos devuelve la posicion de esa letra en el abecedario
        nueva_posicion_letra = int(posicion_letra[0]) + num
        if nueva_posicion_letra > len(abecedario):
            nueva_posicion_letra = nueva_posicion_letra - len(abecedario)
            nueva_letra = abecedario[nueva_posicion_letra]
            print(f"Letra: {letra}, Posición: {posicion_letra}, Nueva posicion: {nueva_posicion_letra}, Nueva letra:{nueva_letra}") #tiene que ser e
            print(f"Longitud abd: {len(abecedario)}")
        else:
            nueva_letra = abecedario[nueva_posicion_letra]
            print(f"Letra: {letra}, Posición: {posicion_letra}, Nueva posicion: {nueva_posicion_letra}, Nueva letra: {nueva_letra}") #posicion de la letra en el abecedario
        #-25???
    
    return ""
print(encriptador_cesar("holaz", 5, ""))
print(encriptador_cesar("holaz", 5, "D"))

# nuevo_mensaje = encriptador_cesar(mensaje, num, encriptar)

# Dar la opcion de hacerlo otra vez