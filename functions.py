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
def letter_idx(letra, lista):
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


# Función empleada en el proyecto 007-Caesar-cipher
def caesar_cipher(mensaje, encriptar, num, abc):
    """
    Esta funcion nos permite cifrar y descifrar un mensaje. Es un encriptador.
    Los param son el mensaje, el número de saltos en la lista, la dirección de los saltos (+/D para encriptar, -/IZQ para desencriptar) y una lista de valores (generalmente un abecedario)
    El funcionamiento interno está explicado con comentarios y también hay un par de prints comentados que pueden usarse para entender el funcionamiento de esta función.
    Internamente utiliza la función pos_letra.
    """
    if encriptar == "D":
        num = -num 
        print(f"\nTu mensaje es {mensaje}, y lo vamos a desencriptar, usando un valor de {num}\n")
    elif encriptar == "C":
        print(f"\nTu mensaje es {mensaje}, y lo vamos a encriptar, usando un valor de {num}\n")
    else:
        print("\nEncriptar debe de ser D o E, la función no admite otras opciones para este parámetro\n")

    lista_mensaje = list(mensaje) #Pasamos de string a list
    nuevo_mensaje_lista = [] #Creamos una lista vacía para el nuevo mensaje

    for letra in lista_mensaje: #Iteramos sobre el mensaje (lista compuesta por cada una de las letras del mensaje a encriptar)

        posicion_letra = letter_idx(letra, abc) #Comparamos cada letra del mensaje con las letras del abecedario, cuando hay coincidencia, nos devuelve el index en el abcedario
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
        
# Función empleada en el proyecto 008-Blind-auction
def add_bid(diccionario):
    """
    Esta funcion nos permite añadir un nuevo par clave-valor a un diccionario.
    """
    pujador = input("Nombre: ")
    puja = input("Puja: ")
    diccionario[pujador] = puja
    return diccionario

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