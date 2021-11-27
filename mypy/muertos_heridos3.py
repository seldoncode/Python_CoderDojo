# Juego de los Muertos y Heridos (Cows and Bulls game)
import random
import os
random.seed()

# Inicializamos variables

m = h = 0                                 # m son los muertos, h son los heridos
tirada = 0
jugando = True
r = []           # matriz resultado: almacena todos los intentos [[XXXX, m, h], [XXXX, m, h]]
digitos = "0123456789"

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

# La máquina elige al azar, sin repetición, los cuatro digitos del nº secreto
# secreto es un string de cuatro dígitos, por ejemplo: "0249"
# secreto = random.sample(range(10), k=4)   # ejemplo: [0, 8, 1, 9]

secreto = "".join(random.choices(digitos, k=4))

# Bucle principal mientras no se acierte el número

while jugando:       # mientras estemos jugando
    
    # Pedimos al jugador su intento
    
    incorrecto = True    # inicialmente pensamos que el número que introduce el jugador es incorrecto

    while incorrecto:
        print("Se sale si se introduce algún caracter no numérico.")
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
            #print("Su intento es: ", intento)
            incorrecto = False

    if not(jugando):
        print("Fin del juego")
        break

    
    


'''
    
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

    if 

    '''