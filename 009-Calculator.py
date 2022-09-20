def inputNaturalOCero(pregunta="Introduce un número entero mayor o igual a cero: "):
    num = input(pregunta)
    if num[0] == "+":
        num = num[1:]
    while len(num) == 0 or num.isnumeric() == False or int(num) < 0:
        print("Necesitas introducir un número igual o mayor que cero")
        num = input(pregunta)
    return int(num)

def operaciones (n1, n2, operador):
    if operacion == "/":
        return print(f"\nLa división es: {n1 / n2}")
    elif operacion == "*":
        return print(f"\nLa multiplicación es: {n1 * n2}")
    elif operacion == "+":
        return print(f"\nLa suma es: {n1 + n2}")
    elif operacion == "-":
        return print(f"\nLa resta es: {n1 - n2}")
    else:
        return print(f"\nSuma: {n1 + n2} \nResta: {n1 - n2} \nMultiplicación: {n1 * n2} \nDivision: {n1 // n2}")

n1 = inputNaturalOCero()
operacion = input("Opciones:\n\n    /\n    *\n    +\n    -\n    Todas\n\nEscoge una operación (/, *, +, -, o todas): ")
n2 = inputNaturalOCero("\nDime un segundo número: ")

operaciones(n1, n2, operacion)

