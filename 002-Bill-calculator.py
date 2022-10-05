print("Welcome to your bill calculator ")

bill = float(input("How much was the bill? "))
tip = input("What percentage would you like to pay as tip? Please add a percentage; e.g. 10% ")
people = int(input("How many people are paying? "))

if tip[-1] == "%":
    tip = tip[:-1]

tip = int(tip)

# Individual bills are calculated dividing bill + tip among the people. This result is then rounded.
print(f"Each person has to pay: {round(((bill + (bill * (tip /100))) / people), 2)} €")