
#MVP, bastantes cosas a mejorar. Este programa permite a varios usuarios realizar subastas, nos devuelve el ganador de la subasta.

diccionario = {}

def nuevos_datos ():
    nombre = input("Nombre: ")
    puja = input("Puja: ")
    diccionario[nombre] = puja
    return diccionario

mas_pujas = "S":
while mas_pujas == "S":
    nuevos_datos()
    mas_pujas = input("¿Hay más pujadores? (S/N)").upper()

print(diccionario)

#comparar values, devolver key del mayor
