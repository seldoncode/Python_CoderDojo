import random
import os
random.seed()

digitos = "0123456789"
numero = ""               # número secreto aleatorio de cuatro dígitos, es um string
muertos = 0
heridos = 0
intento = None            # será el string de 4 dígitos que introduzca el jugador en cada tirada 
resultados = []           # almacena todos los intentos [[XXXX, M, H], [XXXX, M, H]]
salir = False

# Presentación del programa

os.system("clear")

print("**************************************************************************")
print("*                                                                        *")
print("*                  Juego Muertos y Heridos                               *")
print("*                     Tienes 15 intentos                                 *")
print("*                                                                        *")
print("*                 Pulsa ENTER para empezar                               *")
print("*                                                                        *")
print("**************************************************************************")

input()

# Computadora elige al azar los números para adivinar, sin repetición

while len(numero) < 4:
    digito =  random.choice(digitos)
    if digito not in numero:
        numero += digito

# Bucle principal mientras no se acierte el número

while True:
     
    os.system("clear")
     
    print("**********************************************************")
    print("*                   Muertos y Heridos                    *")
    print("**********************************************************")
    print("*           Número       -       Muertos  -  Heridos     *")
    print("*         ----------     -      ---------    -------     *")
                                                                                                                                                                                                                                                                                                                                                                                                                                  
    # Muestra todos los intentos que el usuario ha hecho hasta el momento

    for i in range (len(resultados)):
        plantilla = "*            {}        -          {}     -    {}         *"
        print(plantilla.format(resultados[i][0], resultados[i][1], resultados[i][2]))
        print("*                                                        *")


    # Comprobación de si se ha ganado, y salida del programa en ese caso

    if numero == intento:
        print("*            Has acertado el número. Has ganado.         *")
        print(f"*            Has necesitado {len(resultados)} intentos                  *")
        break

    # Comprobación de los intentos, y salida del programa si agotados

    if len(resultados) >= 15:
        print("*          Has agotado los intentos. Has perdido.        *")
        print(f"*            El número era: {numero}                         *")
        break

    # Bucle para que el usuario elija un número correcto
      
    while True:
        intento = input("=> Introduce intento o (s)alir: ")
        if intento == "s":
            salir = True
            break
        elif len(intento) !=4:
            print("Introduce un número de 4 dígitos.")
        elif intento[0] not in digitos or intento[1] not in digitos or \
             intento[2] not in digitos or intento[3] not in digitos:
            print("Introduce cuatro dígitos solo del 0 al 9.")
        elif intento[0]==intento[1] or intento[0]==intento[2] or intento[0]==intento[3] or \
             intento[1]==intento[2] or intento[1]==intento[3] or intento[2]==intento[3]:
            print("No se pueden repetir cifras. Inténtelo de nuevo.")
        else:
            break

    # Si la bandera salir es True salimos del programa

    if salir:
        print("La solución era:", numero)
        break   # salimos del bucle principal

    # Bucle para comprobar el número de muertos y heridos

    for i in range(4):
        if intento[i] in numero:
            if intento[i]  == numero[i]:
                muertos += 1
            else:
                heridos += 1

    # Añadimos el intento y su resultado a la lista de resultados

    resultados.append([intento, muertos, heridos])

    # Reiniciamos las variables a cero para nuevo intento

    muertos = 0
    heridos = 0