from functions import nuevos_datos

# MVP, bastantes cositas por mejorar. 
# Este programa permite a varios usuarios realizar subastas, nos devuelve el ganador de la subasta.

diccionario = {}

# Damos la opción de crear más entradas/participantes en la puja
mas_pujas = "S"
while mas_pujas == "S":
    nuevos_datos(diccionario)
    mas_pujas = input("¿Hay más pujadores? (S/N) ").upper()

# Creamos dos listas, una con los valores y otro con las claves
lista_valores = list(diccionario.values())
lista_pujadores = list(diccionario.keys())

# Obtenemos la puja mayor usando el método max
valor_mayor = max(lista_valores)

# Empleamos index para conseguir la clave del valor ganador, que es el ganador de la puja
print(f"El ganador de la puja es: {lista_pujadores[lista_valores.index(valor_mayor)]}")

