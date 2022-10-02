# Aproximación a la POO... Bastantes cosas aún por mejorar!

# POR HACER
# *********
# Mejorar mostrar() -> dejarlo todo en un solo print. No es fácil ni banal pero te lo dejo para que le des un pensao
# y también está pidiendo a gritos un método operar(signo) que una las dos líneas c.operacion = signo + c.mostrar()


from functions import input_natural_o_cero

# Creamos la clase
class calculadora:

    def __init__(self, n1, n2):
        self.num1 = float(n1) 
        self.num2 = float(n2) 
        self.operacion = ""

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def dividir(self):
        return self.num1 / self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def mostrar(self):

        if self.operacion not in ('+', '-', '*', '/'):
            raise Exception("Operacion debe ser +, -, * o '/'")

        if operacion == "+":
            self.sumar()
        elif operacion == "-":
            self.restar()
        elif operacion == "/":
            self.dividir()
        else:
            self.multiplicar()
#PRINTS?!


operaciones_disponibles = ["+", "-", "/", "*"]

num1= input_natural_o_cero ()

operacion = input(f"\nOpciones disponibles:\n\n  {operaciones_disponibles[0]}\n  {operaciones_disponibles[1]}\n  {operaciones_disponibles[2]}\n  {operaciones_disponibles[3]}\n\nTu opción: ")

while not operacion in operaciones_disponibles:
     operacion = input(f"\nTienes que seleccionar una de las siguientes opciones:\n\n  {operaciones_disponibles[0]}\n  {operaciones_disponibles[1]}\n  {operaciones_disponibles[2]}\n  {operaciones_disponibles[3]}\n\nTu opción: ")

num2 = input_natural_o_cero ("\nDime un segundo número: ")

mi_calculadora = calculadora(num1, num2)

