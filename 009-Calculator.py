def inputNaturalOCero(pregunta="Introduce un número entero mayor o igual a cero: "):
    num = input(pregunta)
    if num[0] == "+":
        num = num[1:]
    while len(num) == 0 or num.isnumeric() == False or int(num) < 0:
        print("Necesitas introducir un número igual o mayor que cero")
        num = input(pregunta)
    return int(num)

def multiplicacion (n1, n2):
    return print(f"\nLa multiplicación de {n1} y {n2} es: {n1 * n2}")

def division (n1, n2):
    return print(f"\nLa división de {n1} y {n2} es: {n1 / n2}")

def suma (n1, n2):
    return print(f"\nLa suma de {n1} y {n2} es: {n1 + n2}")

def resta (n1, n2):
    return print(f"\nLa resta de {n1} y {n2} es: {n1 - n2}")

operaciones = {
    "/" : division,
    "*" : multiplicacion,
    "+" : suma,
    "-" : resta
}

n1 = inputNaturalOCero ()

operacion = input ("\nOpciones disponibles:\n\n    /\n    *\n    +\n    -\n\nTu opción: ")

while not operacion in operaciones.keys():
     operacion = input ("\nTienes que seleccionar una de las siguientes opciones:\n\n    /\n    *\n    +\n    -\n\nTu opción: ")

n2 = inputNaturalOCero ("\nDime un segundo número: ")

operacion_a_realizar = operaciones[operacion]
operacion_a_realizar (n1, n2)
