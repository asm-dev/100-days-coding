from functions import input_natural_o_cero

# Creamos la clase
class Calculator:

    def __init__(self, n1, n2, operator):
        self.num1 = float(n1) 
        self.num2 = float(n2) 
        self.operator = operator

    def operation(self, operator):
        if operator == "+":
            return self.num1 + self.num2
        elif operator == "-":
            return self.num1 - self.num2
        elif operator == "*":
            return self.num1 * self.num2
        elif operator == "/":
            return self.num1 / self.num2
        else:
            return "Operation not supported"


num1 = input_natural_o_cero ()

available_operations = ["+", "-", "/", "*"]

operator = input(f"\nAvailable options:\n\n  {available_operations[0]}\n  {available_operations[1]}\n  {available_operations[2]}\n  {available_operations[3]}\n\nTu opción: ")
while not operator in available_operations:
    operator = input(f"\nYou have to select one of these options:\n\n  {available_operations[0]}\n  {available_operations[1]}\n  {available_operations[2]}\n  {available_operations[3]}\n\nTu opción: ")

num2 = input_natural_o_cero ("\nPlease introduce a second number: ")

calculator = Calculator(num1, num2, operator)
print(f"The operation result is: {calculator.operation(calculator.operator)}")


# my_calculator1 = Calculator(2, 2, "+")
# my_calculator2 = Calculator(2, 2, "-")
# my_calculator3 = Calculator(2, 2, "/")
# my_calculator4 = Calculator(2, 2, "*")
# my_calculator5 = Calculator(2, 2, "A")

# print(f"NUM 1: {my_calculator1.num1}, NUM 2: {my_calculator1.num2}, OPERATOR: {my_calculator1.operator}")
# print(f"RESULT OPERATION: {my_calculator1.operation(my_calculator1.operator)}")
# print(f"NUM 1: {my_calculator2.num1}, NUM 2: {my_calculator2.num2}, OPERATOR: {my_calculator2.operator}")
# print(f"{my_calculator2.operation(my_calculator2.operator)}")
# print(f"NUM 1: {my_calculator3.num1}, NUM 2: {my_calculator3.num2}, OPERATOR: {my_calculator3.operator}")
# print(f"{my_calculator3.operation(my_calculator3.operator)}")
# print(f"NUM 1: {my_calculator4.num1}, NUM 2: {my_calculator4.num2}, OPERATOR: {my_calculator4.operator}")
# print(f"{my_calculator4.operation(my_calculator4.operator)}")
# print(f"NUM 1: {my_calculator5.num1}, NUM 2: {my_calculator5.num2}, OPERATOR: {my_calculator5.operator}")
# print(f"{my_calculator5.operation(my_calculator5.operator)}")