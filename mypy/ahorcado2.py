# resuelto con listas
import random
import os
random.seed()
palabras = ['AUSTRALIA','GANADERIA','ASOMBROSO','EXTRAORDINARIO','AGUAFIESTAS',
            'IMPRESIONANTE','ESPAÑA','ROMANTICO','HISTORICO','NEANDERTAL']
palabra = list(random.choice(palabras))   # convertimos la palabra en una lista

horca = ["          !=======N",
         "                  N",
         "                  N",
         "                  N",
         "                  N",
         "                  N",
         "                  N",
         "     _____________N"]

ahorcado = ["          !=======N",
            "          O       N",
            "        / | \     N",
            "        \ | /     N",
            "         / \      N",
            "        /   \     N",
            "       _\   /_    N",
            "     _____________N"]


letras_todas = []         # todas las letras dichas por el usuario en una lista
fallos = 1                # se inicial en 1 para que la lista ahorcado muestre ya la primera línea de caracteres

resultado = []            # es una lista mezcla de letras acertadas y guiones bajos

for i in range(len(palabra)):
    resultado.append("_")

# Bucle principal del juego

while True:
    
    os.system("clear")

    print()
    print("************************************")
    print("***      JUEGO DEL AHORCADO      ***")
    print("************************************")
    print()

    for i in range(fallos):
        print(ahorcado[i])
    for i in range (len(horca)-fallos):
        print(horca[i+fallos])

    print()

    # Mostramos el resultado que se va obteniendo

    print("       ", end=" ")     # para dejar un pequeño espacio
    for i in resultado:
        print(i, end=" ")

    print()
    print()

    # Comprobamos si se ha acrtado la palabra o se han terminado los intentos

    if resultado == palabra:
        print("***          HAS GANADO          ***")
        break

    if fallos > 6:
        print("La palabra era:", "".join(palabra))
        print("***          HAS PERDIDO         ***")
        break

    # Bucle para que el usuario elija una letra


    while True:
        letra_usuario = input("Introduce una letra (sin tilde): ").upper()
        if len(letra_usuario) != 1:
            print("Introduce una letra.")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la has dicho.")
        elif letra_usuario not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
            print("Introduce una letra.")
        else:
            letras_todas.append(letra_usuario)
            break
    
    # Comprobamos si la letra dicha está en la palabra, si está la sustituimos por el guión
    for i in range(len(palabra)):
        if palabra[i] == letra_usuario:
            resultado[i] = letra_usuario
    
    if letra_usuario not in palabra:
        fallos += 1

    print()
    print()