print('''
*******************************************************************************\n
    .-------------'```'----....,,__                        _,
   |                               `'`'`'`'-.,.__        .'(
   |                                             `'--._.'   )
   |                                                   `'-.<
   \               .-'`'-.                            -.    `(
    \               -.o_.     _                     _,-'`\    |
     ``````''--.._.-=-._    .'  \            _,,--'`      `-._(
       (^^^^^^^^`___    '-. |    \  __,,..--'                 `
        `````````   `'--..___\    |`
                              `-.,'                   EN BÚSQUEDA DE LA BALLENA

*******************************************************************************
''')

print('Bienvenido a "En búsqueda de la ballena", ¡una historia fascinante! \nTu misión es encontrar la ballena.')

opcion1 = input("\n\n\nEstás regresando a puerto, pero dudas si poner rumbo noroeste o noroeste. (NO/NE) ").lower()
if opcion1 == "no":
  opcion2 = input("\nMientras vuelves al puerto, empiezas a ver los colores del cielo cambiar. Es un atardecer precioso. ¿Quieres quedarte a verlo un poco más? (S/N) ").lower()
  if opcion2 == "s":
    opcion3 = input("\nEs una noche cálida de verano, y ya casi llegando al puerto, tranquilo tras un maravilloso atardecer, desde la proa, sopesas la idea de darte un baño. Tienes tres opciones, ignorar tus deseos y regresar a puerto, impulsivamente desnudarte y tirarte al agua sin darle mucha vuelta, terminar de ver el atardecer un poquito más y tirarte al agua. ¿Qué opción escoges? (1/2/3/otra) ").lower()
    if opcion3 == "1":
      print("\nRefunfuñando, vuelves a puerto, sin haber avistado ninguna ballena. Vuelve a intentarlo.")
    elif opcion3 == "2":
      print("\nTe lanzas al agua y disfrutas muchísimo del chapuzón, estás tan entretenido nadando que no te das ni cuenta de que una ballena está pasando detrás de tu barco. Regresas a casa sin haber visto la ballena. Vuelve a intentarlo.")
    elif opcion3 == "3":
      print("\nMientras ves el sol en el horizonte, con calma, al ritmo del sol, te desnudas y bajas al agua. Ya en el agua, te das cuenta de que hay unas ondas extrañas. Sigues las ondas a nado, y según das la vuelta al barco, de repente, ves un chorro de agua gigantesco, seguido por una cola enorme que, como el sol, se mete en el agua ¡Es una ballena!")
    else:
      print("\nDesafortunadamente, no avistas ninguna ballena. No obstante, regresas contento a puerto. Vuelve a intentarlo, para encontrar la ballena.")
  else:
    print("\nLlegas sano y salvo a puerto, tras ver un maravilloso atarceder, pero no avistas ninguna ballena. Vuelve a intentarlo.")
else:
  print("\nLlegas sano y salvo a puerto, pero no avistas ninguna ballena. Vuelve a intentarlo.")