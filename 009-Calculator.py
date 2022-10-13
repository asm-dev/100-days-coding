from functions import input_natural_o_cero

def multiply(n1, n2):
    return print(n1 * n2)

def divide(n1, n2):
    return print(n1 / n2)

def add(n1, n2):
    return print(n1 + n2)

def rest(n1, n2):
    return print(n1 - n2)

operators = {
    "/" : divide,
    "*" : multiply,
    "+" : add,
    "-" : rest
}

n1 = input_natural_o_cero()

op = input("\nAvailable options:\n\n    /\n    *\n    +\n    -\n\nYour choice: ")

while not op in operators.keys():
     op = input("\nThese are the available choices:\n\n    /\n    *\n    +\n    -\n\nPlease introduce your choice: ")

n2 = input_natural_o_cero("\nPlease introduce a second number: ")

operators[op](n1, n2)
