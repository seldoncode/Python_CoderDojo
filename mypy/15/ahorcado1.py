# resuelto con strings
import random
import os
random.seed()
palabras = ['AUSTRALIA','GANADERIA','ASOMBROSO','EXTRAORDINARIO','AGUAFIESTAS',
            'IMPRESIONANTE','ESPAÑA','ROMANTICO','HISTORICO','NEANDERTAL']
palabra = random.choice(palabras)

fallo0 = '''
           !===N
               N
               N
               N
       =========
'''

fallo1 = '''
           !===N
           O   N
               N
               N
       =========
'''

fallo2 = '''
           !===N
          _O   N
               N
               N
       =========
'''

fallo3 = '''
           !===N
          _O_  N
               N
               N
       =========
'''

fallo4 = '''
           !===N
          _O_  N
           |   N
               N
       =========
'''

fallo5 = '''
           !===N
          _O_  N
           |   N
          /    N
       =========
'''

fallo6 = '''
           !===N
          _O_  N
           |   N
          / \  N
       =========
'''

letras_correctas = ""     # letras correctas dichas por el usuario
letras_todas = ""         # todas las letras dichas por el usuario
fallos = 0                # contador de fallos

while True:
    
    os.system("clear")

    print()
    print("************************************")
    print("***      JUEGO DEL AHORCADO      ***")
    print("************************************")
    print()

    if fallos == 0:
        print(fallo0)
    elif fallos == 1:
        print(fallo1)
    elif fallos == 2:
        print(fallo2)
    elif fallos == 3:
        print(fallo3)
    elif fallos == 4:
        print(fallo4)
    elif fallos == 5:
        print(fallo5)
    elif fallos == 6:
        print(fallo6)

    print()

    # Mostramos las letras acertadas y guiones bajos en las no acertadas

    resultado = ""      # es una mezcla de letras acertadas y guiones bajos

    for letra in palabra:
        if letra in letras_correctas:
            resultado += letra
        else:
            resultado += "_"

    print(f"           {resultado}")

    print()
    print()

    # Comprobamos si se ha acertado la palabra o se han terminado los intentos

    if resultado == palabra:
        print("***       HAS  GANADO     ***")
        break

    if fallos == 6:
        print("La palabra era:", palabra)
        print("***       HAS  PERDIDO     ***")
        break

    # Bucle para que el usuario teclee una letra que cumpla los requisitos

    while True:
        letra_usuario = input("Introduce una letra (sin tilde): ").upper()
        if len(letra_usuario) != 1:
            print("Introduce una letra.")
        elif letra_usuario in letras_todas:
            print("Esa letra ya la has dicho.")
        elif not letra_usuario.isalpha():
            print("Introduce una letra.")
        else:
            letras_todas += letra_usuario
            break
    
    # Comprobamos si la letra dicha está en la palabra

    if letra_usuario not in palabra:
        fallos += 1
    else:
        letras_correctas += letra_usuario