#Función empleada en el proyecto 006-Hangman
def comprueba_letra (palabra, letra):
    """
    Esta función nos informa de la posición de una letra en una palabra.
    Si la letra se encuentra en la palabra, nos devuelve una lista con los valores de la posición,
    por ejemplo comprueba_letra("casa", "a") nos devuelve [1, 3].
    Si la letra no se encuentra en la palabra, nos devuelve una lista vacía, []
    """
    posicion = []
    for n in range(len(palabra)):
        if palabra[n] == letra:
            posicion.append(n)
    return posicion


#Función empleada en el proyecto 007-Caesar-cipher, dentro de la funcion encriptador_cesar
def pos_letra (letra, lista):
    """
    Esta función compara una letra con los elementos de una lista.
    Se itera la lista y se compara cada uno de los elementos de la lista con la letra.
    Si algún elemento de la lista es igual a la letra, se añade a la lista vacía posiciones el index en la lista de ese elemento.
    Esta función se emplea dentro de la función César para conseguir el idx en el abecedario de una letra.
    """
    posiciones = []
    for i in lista:
        if letra == i:
            posiciones.append(lista.index(i))
    return posiciones #Nos devuelve una lista, podemos conseguir el item con posiciones[0]


#Función empleada en el proyecto 007-Caesar-cipher
def encriptador_cesar (mensaje, encriptar, num, abc):
    """
    Esta funcion nos permite cifrar y descifrar un mensaje. Es un encriptador.
    Los param son el mensaje, el número de saltos en la lista, la dirección de los saltos (+/D para encriptar, -/IZQ para desencriptar) y una lista de valores (generalmente un abecedario)
    El funcionamiento interno está explicado con comentarios y también hay un par de prints comentados que pueden usarse para entender el funcionamiento de esta función.
    Internamente utiliza la función pos_letra.
    """
    if encriptar == "D":
        num = -num 
        print(f"\nTu mensaje es {mensaje}, y lo vamos a desencriptar, usando un valor de {num}\n")
    elif encriptar == "E":
        print(f"\nTu mensaje es {mensaje}, y lo vamos a encriptar, usando un valor de {num}\n")
    else:
        print("\nEncriptar debe de ser D o E, la función no admite otras opciones para este parámetro\n")

    lista_mensaje = list(mensaje) #Pasamos de string a list
    nuevo_mensaje_lista = [] #Creamos una lista vacía para el nuevo mensaje

    for letra in lista_mensaje: #Iteramos sobre el mensaje (lista compuesta por cada una de las letras del mensaje a encriptar)

        posicion_letra = pos_letra(letra, abc) #Comparamos cada letra del mensaje con las letras del abecedario, cuando hay coincidencia, nos devuelve el index en el abcedario
        nueva_posicion_letra = posicion_letra[0] + num #Añade el valor al index de la letra del mensaje

        if nueva_posicion_letra > len(abc): #Puede ser que la nueva posición sea mayor que la longitud del abecedario, por ejemplo, index de Z + 5
            nueva_posicion_letra = nueva_posicion_letra - len(abc)
            nueva_letra = abc[nueva_posicion_letra]

            # PRINTS PARA ENTENDER QUÉ PASA AQUÍ:
            # print(f"Letra: {letra}, Posición: {posicion_letra}, Nueva posicion: {nueva_posicion_letra}, Nueva letra:{nueva_letra}") #tiene que ser e
            # print(f"Longitud abd: {len(abecedario)}")

        else:
            nueva_letra = abc[nueva_posicion_letra]
            # PRINT PARA ENTENDER QUÉ PASA AQUÍ:
            # print(f"Letra: {letra}, Posición: {posicion_letra}, Nueva posicion: {nueva_posicion_letra}, Nueva letra: {nueva_letra}") #posicion de la letra en el abecedario
        
        nuevo_mensaje_lista.append(nueva_letra)
        nuevo_mensaje = ''.join(nuevo_mensaje_lista)

    return nuevo_mensaje
        