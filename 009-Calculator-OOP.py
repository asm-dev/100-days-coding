# Un poco de mezcla entre programación funcional y programación orientada a objetos, para ir probando la POO en Python...

def inputNaturalOCero(pregunta="Introduce un número entero mayor o igual a cero: "):
    num = input(pregunta)
    if num[0] == "+":
        num = num[1:]
    while len(num) == 0 or num.isnumeric() == False or int(num) < 0:
        print("Necesitas introducir un número igual o mayor que cero")
        num = input(pregunta)
    return int(num)

# Creamos la clase
class calculadora:

    def __init__(self, n1, n2):
        self.num1 = int(n1) # Float?
        self.num2 = int(n2) 

    def sumar(self):
        print(f"\nLa suma de {self.num1} y {self.num2} es: {self.num1 + self.num2}")

    def restar(self):
        print(f"\nLa resta de {self.num1} y {self.num2} es: {self.num1 - self.num2}")

    def dividir(self):
        print(f"\nLa división de {self.num1} y {self.num2} es: {self.num1 / self.num2}")

    def multiplicar(self):
        print(f"\nLa multiplicación de {self.num1} y {self.num2} es: {self.num1 * self.num2}")

operaciones_disponibles = ["+", "-", "/", "*"]

num1= inputNaturalOCero ()

operacion = input(f"\nOpciones disponibles:\n\n  {operaciones_disponibles[0]}\n  {operaciones_disponibles[1]}\n  {operaciones_disponibles[2]}\n  {operaciones_disponibles[3]}\n\nTu opción: ")

while not operacion in operaciones_disponibles:
     operacion = input(f"\nTienes que seleccionar una de las siguientes opciones:\n\n  {operaciones_disponibles[0]}\n  {operaciones_disponibles[1]}\n  {operaciones_disponibles[2]}\n  {operaciones_disponibles[3]}\n\nTu opción: ")

num2 = inputNaturalOCero("\nDime un segundo número: ")

mi_calculadora = calculadora(num1, num2)

if operacion == operaciones_disponibles[0]:
    mi_calculadora.sumar()
elif operacion == operaciones_disponibles[1]:
    mi_calculadora.restar()
elif operacion == operaciones_disponibles[2]:
    mi_calculadora.dividir()
else:
    mi_calculadora.multiplicar()
