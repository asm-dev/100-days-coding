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