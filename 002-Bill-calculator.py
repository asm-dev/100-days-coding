print("Vamos a calcular cuánto ponemos de propina entre varias personas ")
cuenta = float(input("¿Cuánto fue la cuenta? "))
propina = input("¿Qué porcentaje queremos pagar? 10%, 12%, or 15%? ")
personas = int(input("¿Entre cuántas personas se divide la cuenta? "))

if propina[-1] == "%":
    propina = propina[:-1]
    propina = int(propina)
else:
    propina = int(propina)

total_propina = cuenta * (propina / 100)
total_cuenta = cuenta + total_propina
pago_persona = round(total_cuenta / personas, 2)

print(f"Cada persona debe pagar: {pago_persona}€")