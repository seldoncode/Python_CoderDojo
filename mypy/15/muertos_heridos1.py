import random
random.seed()
print("============= Juego de los Muertos y Heridos =============")
print("Dispone de 15 intentos para adivinar el número secreto de cuatro dígitos sin repetición.")
print("Puede salir en cualquier momento tecleando cualquier caracter no numérico.")
secreto = [str(x) for x in random.sample(range(10), 4)]
#print(secreto)         # descomentar esta línea para hacer trampas
tirada = 0
jugando = True
while jugando:
  tirada += 1
  incorrectos = True    # inicialmente pensamos que los número que dice el jugador están incorrectos
  while incorrectos:    # mientras pensemos que están incorrectos pediremos que introduzca un número sin repetición y de 4 dígitos
    n = input(f"Tirada {tirada}: Diga un número de cuatro dígitos entre 0 y 9, sin repetir digitos: ")
    if not(n.isnumeric()) or len(n) != 4:
      print("Fin del juego.")
      incorrectos=False       # para salirnos del while interno
      jugando=False           # ya nos queremos salir
    intento = list(n)    # ['1', '2', '3', '4']
    if sorted(intento) == sorted(list(set(intento))): # para evitar que el número que diga el jugador tenga repetidos
      incorrectos = False
  if not(jugando): break      # si queremos salir, ya hemos dicho que jugando=False y ya nos saliemos del while principal
  resultado = ""
  m = h = 0                   # inicializamos los muertos y heridos
  for i in range(4):
    if intento[i] in secreto: h += 1
    if intento[i] == secreto[i]: m += 1; h -= 1
    resultado = f"{m}M{h}H"
  print(f"{intento[0]+intento[1]+intento[2]+intento[3]} : {resultado}")
  if resultado == "4M0H":
    print(f"Felicidades: ha adivinado el número secreto {secreto[0]+secreto[1]+secreto[2]+secreto[3]} en {tirada} tiradas.")
    jugando = False
  elif tirada==15:
    print("Se han agotado los 15 intetos. Fin del juego.")
    jugando = False