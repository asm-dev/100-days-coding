import random

nombre = input("¿Cómo te llamas? ")
print(f"\nHola {nombre}, vamos a generar un nombre aleatorio para tu artículo o disertación. \nEl nombre de tu disertación es:")

opciones_inicio = ["Análisis cualitativo sobre", "Estudio sobre", "Exploración de"]
opciones_medio = ["las carencias de", "los sublimes esfuerzos de", "la exposición a"]
opciones_final = ["las singularidades cuánticas", "los tomates", "los procesos mitocondriales"]


def crear_historia(lista1, lista2, lista3, autor):
    inicio = random.choice(lista1)
    medio = random.choice(lista2)
    final = random.choice(lista3)
    historia = '"' + "\x1B[3m" + inicio + " " + medio + " " + final + "\x1B[0m" + '"'
    return print(f"\n{historia} {autor}")

crear_historia(opciones_inicio, opciones_medio, opciones_final, nombre)

while input("\n¿Quieres una nueva sugerencia? (S/N) ") == "S":
    crear_historia(opciones_inicio, opciones_medio, opciones_final, nombre)
    input("\n¿Quieres una nueva sugerencia? (S/N) ")