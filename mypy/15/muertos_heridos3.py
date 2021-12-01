#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Juego de los Muertos y Heridos (Cows and Bulls game)
import random
import os
random.seed()

# Inicializamos variables

intento = None   # intento será el string que teclee el jugador
tirada = 0
jugando = True
r = []           # matriz resultado: almacena todos los intentos [[XXXX, m, h], [XXXX, m, h]]

# Presentación del programa

os.system("clear")

print("**************************************************************************")
print("*                                                                        *")
print("*                  Juego Muertos y Heridos                               *")
print("*                     Tienes 15 intentos                                 *")
print("*                                                                        *")
print("*                 Pulsa ENTER para empezar                               *")
print("*                                                                        *")
print("*         Se sale si se introduce algún caracter no numérico             *")
print("**************************************************************************")

input()

# La máquina elige al azar, sin repetición, los cuatro digitos del nº secreto

secreto = ''.join(random.sample("0123456789", 4)) # es un string
#print(secreto)           # descomentar esta línea para hacer trampas

# Bucle principal mientras no se acierte el número

while jugando:       # mientras estemos jugando
    
    # Mostramos los resultados en una tabla

    os.system("clear")
    
    print("**********************************************************")
    print("*                   Muertos y Heridos                    *")
    print("**********************************************************")
    print("*           Número       -       Muertos  -  Heridos     *")
    print("*         ----------     -      ---------    -------     *")

    # Muestra todos los intentos que el usuario ha hecho hasta el momento

    for i in range (len(r)):
        print(f"*            {r[i][0]}        -          {r[i][1]}     -    {r[i][2]}         *")
        print("*                                                        *")

    # Comprobación de si se ha ganado, y salida del programa en ese caso

    if intento == secreto:
        print("*            Has acertado el número. Has ganado.         *")
        print(f"*                 Has necesitado {len(r)} intentos.                *")
        break

    # Comprobación de los intentos, y salida del programa si agotados

    if len(r) >= 15:
        print("*          Has agotado los intentos. Has perdido.        *")
        print(f"*            El número era: {secreto}                         *")
        break

    # Bucle para que el usuario elija un número correcto
    
    incorrecto = True    # inicialmente pensamos que el número que introduce el jugador es incorrecto

    while incorrecto:
        print()
        intento = input("=> Introduce cuatro dígitos sin repetir: ")
        if not(intento.isnumeric()):
            print("Al introducir un caracter no numérico el juego termina.")
            print(f"El número secreto era {secreto}.")
            incorrecto = False
            jugando = False   # FIN DEL JUEGO
        elif len(intento)!=4:
            print("El número introducido debe tener cuatro dígitos.")
        elif sorted(intento) != sorted(set(intento)):
            print("No debe haber cifras repetidas.")
        else:
            print("Su intento es: ", intento)
            incorrecto = False

    if not(jugando):
        print("Fin del juego")
        break

    # Se calculan los Muertos y Heridos

    m = h = 0        # m son los muertos, h son los heridos
    for i in range(4):
        if intento[i] in secreto:
            if intento[i] == secreto[i]:
                m += 1
            else:
                h += 1

    # Añadimos el intento y el resultado a la matriz de resultados

    r.append([intento, m, h])