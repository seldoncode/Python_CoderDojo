'''
Juego: Muertos y heridos (Mastermind)
'''

import random
import os

digitos = "0123456789"
numero = ""              # número secreto
muertos = 0
heridos = 0
intento = None
intentos = []   # recoge todos los intentos indicando cuantos muertos y heridos hay Ejemplo: [[1234,1,0], [5678,2,1], [5617,2,2]]
salir = False

# Presentación del programa

os.system("clear")

print("********************************************************")
print("*                                                      *")
print("*                Juego Muertos y Heridos               *")
print("*                 Dispone de 15 intentos               *")
print("*                                                      *")
print("*                Pulse ENTER para empezar              *")
print("*                                                      *")
print("********************************************************")

input()       # Está esperando hasta que se pulsa ENTER

# Generamos el número aleatorio secreto

while len(numero) < 4:
    digito = random.choice(digitos)
    if digito not in numero:
        numero += digito

# Bucle principal mientras no se acierte el número

while True:

    os.system("clear")
    
    print("********************************************************")
    print("*                  MUERTOS Y HERIDOS                   *")
    print("********************************************************")
    print("*           NUMERO       -       M  .  H               *")
    print("*          --------      -     ------------            *")

    # Mostramos todos los intentos que el usuario ha hecho hasta el momento

    for i in range(len(intentos)):
        print(f"*           {intentos[i][0]}         -      {intentos[i][1]} - {intentos[i][2]}              *")
    print("*                                                      *")


    # Comprobación de si se ha ganado, y salida del programa en ese caso

    if numero == intento:
            print("*         Has acertado el número. Has ganado.          *")
            print(f"*           Has necesitado {len(intentos)} intentos.                   *")
            break

    # Comprobación de los intentos, y salida del programa si agotados

    if len(intentos) >= 15:
        print("*        Has agotado los intentos. Has perdido.        *")
        print(f"*                El número era: {numero}                   *")
        break

    # Bucle para que el usuario elija un número correcto

    while True:
        intento = input("=> Introduzca su intento ('q' para salir): ")
        if intento == "q":
            salir = True       # bandera para luego salir del bucle principal
            break              # para salir del while interno
        elif 











