import random

#Transformador de elecciones de número al valor (Piedra, papel o tijera)
def conversion (opcion):
    if opcion == 1:
        return "Piedra"
    elif opcion == 2:
        return "Papel"
    else:
        return "Tijera"

#Comparador de elecciones
def comparacion (opt1, opt2):
    if opt1 == 1 and opt2 == 3:
        return True
    elif opt1 == 2 and opt2 == 1:
        return True
    elif opt1 == 3 and opt2 == 2:
        return True
    return False

score = 0
jugar = True

while jugar:
    
    #Pedimos datos
    opcion_usuario = input("\n¿Qué escoges, piedra, papel o tijera? (1/2/3) ")

    while opcion_usuario != "1" and opcion_usuario != "2" and opcion_usuario != "3":
        print("\nDebes seleccionar 1, 2 o 3, dependiendo de tu elección.")
        opcion_usuario = input("¿Qué escoges, piedra, papel o tijera? (1/2/3) ")

    opcion_usuario = int(opcion_usuario)
    opcion_ordenador = random.choice(range(1,4))

    #Mostramos las elecciones de cada uno
    print(f"Tu elección es: {conversion(opcion_usuario)}")
    print(f"La elección del ordenador es: {conversion(opcion_ordenador)}\n")

    #Evaluamos si el ordenador o el usuario gana
    usuario_vs_ordenador = comparacion (opcion_usuario, opcion_ordenador)
    ordenador_vs_usuario = comparacion (opcion_ordenador, opcion_usuario)

    #Mostramos los resultados 
    #Modificamos y mostramos el score
    if usuario_vs_ordenador == True:
        print("Has ganado")
        score += 1
    elif ordenador_vs_usuario == True:
        print ("Has perdido")
        score -= 1
    else:
        print("Vuelvelo a intentar")

    print(f"Tu score es: {score}")

    de_nuevo = input("\n¿Quieres jugar de nuevo? (S/N) ")
    if de_nuevo == "N":
        jugar = False
    
