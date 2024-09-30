#--------------------------------------------
#Nombre: Paloma González-Ripoll Cano
#Curso: 1º DAW
#Título: Práctica 3. Juego Ruleta modificado
#--------------------------------------------

#Importamos el módulo random que nos va a ayudar a elegir números aleatoriamente y el módulo os para poder limpiar la pantalla
import random
import os

jugadores = []
frase = ""
compradas = ""
acertadas = ""
ganado = 0


def crearJuego(fraseO,numJugadores):
    frase = fraseO
    numJugadores

def oculta(frase, compradas, acertadas):
    fraseoculta = ""
    for letra in frase:
        if letra in "AEIOU" and letra not in compradas:
            fraseoculta += "*"
        elif letra in "BCDFGHJKLMNÑPQRSTVWXYZ" and letra not in acertadas:
            fraseoculta += "*"
        else:
            fraseoculta += letra
    return fraseoculta

def tirarRuleta():
    tirada = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if tirada == 1:
        opcion = 1
        ganado = 0
        return opcion, ganado
    elif tirada == 2:
        opcion = 2
        ganado = ganado*2
        return opcion, ganado
    elif tirada == 3:
        opcion = 3
        return opcion
    elif tirada == 4:
        opcion = 4
        precio = 0
        return opcion, precio
    elif tirada == 5:
        opcion = 5
        precio = 25
        return opcion, precio
    elif tirada == 6:
        opcion = 6
        precio = 50
        return opcion, precio
    elif tirada == 7:
        opcion = 7
        precio = 75
        return opcion, precio
    elif tirada == 8:
        opcion = 8
        precio = 100
        return opcion, precio
    elif tirada == 9:
        opcion = 9
        precio = 150
        return opcion, precio
    elif tirada == 10:
        opcion = 10
        precio = 200
        return opcion, precio

def nuevoJugador(nombre):
    jugadores.append(nombre)


def menu(opcion):
    print("\n1.Decir letra")
    print("2.Comprar vocal")
    print("3.Resolver")
    print("0.Salir")
    opcion = input("\nElije una opción del menú: ")
    return opcion

def decirletra(letra):
    if letra in "BCDFGHJKLMNÑPQRSTVWXYZ" and letra in frase and letra not in acertadas:
        acertadas += letra
        ganado += (precio * frase.count(letra))
        print("\nEsta letra aparece " + str(frase.count(letra)) + " vez(ces) en la frase.")
    elif letra in acertadas:
        print("\nEsa consonante ya se ha acertado antes. Prueba otra vez.")
    elif len(letra) > 1:
        print("\nSólo puedes meter una letra.")
    elif letra not in "BCDFGHJKLMNÑPQRSTVWXYZ":
        print("\nEso no es una consonante.")
    else:
        print("\nEsa consonante no está en la frase.")
    input("\nPulse intro para continuar...")
    os.system("cls")


print("¡BIENVENIDOS AL JUEGO DE LA RULETA!")
print("Instrucciones: \nEs un juego de palabras donde se muestra una frase con letras ocultas. \nLos jugadores proponen letras o intentan adivinar la frase completa para ganar dinero. \nPueden elegir entre: \n1.Decir una consonante para obtener dinero si está en la frase. \n2.Comprar una vocal por un coste fijo de 10€. \n3.Resolver la frase para llevarse el premio acumulado. \nEl objetivo es adivinar la frase completa para ganar dinero.")
input("Pulse intro para continuar.")     
os.system("cls")
print("\nA continuación vamos a registrar al o los jugador/es: ")
nombre = input("Diga el nombre del jugador: ")
nuevoJugador(nombre)
respuesta = input("¿Quiere seguir registrando jugadores? (si/no): ")
if respuesta == "si":
    nombre = input("Diga el nombre del jugador: ")
    nuevoJugador(nombre)
elif respuesta == "no":
    print("Vamos a definir la frase a acertar: ")
    frase = input("\nFrase a adivinar: ").upper()
    os.system("cls")
    frase = frase.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')


while True:
    print("\n\n")
    print("-"*40)
    print(oculta(frase, compradas, acertadas))
    print("-"*40)
    print("\nLlevas ganado " + str(ganado) + "€")
    tirarRuleta()
    opcion = ""
    menu(opcion)
    
    if opcion == "1":
            letra = input("\nIntroduce una consonante: ").upper()
            if letra in "BCDFGHJKLMNÑPQRSTVWXYZ" and letra in frase and letra not in acertadas:
                precio = random.choice([0, 25, 50, 75, 100])
                print("\nEsta letra vale " + str(precio) + "€")
                acertadas += letra
                ganado += (precio * frase.count(letra))
                print("\nEsta letra aparece " + str(frase.count(letra)) + " vez(ces) en la frase.")
            elif letra in acertadas:
                print("\nEsa consonante ya se ha acertado antes. Prueba otra vez.")
            elif len(letra) > 1:
                print("\nSólo puedes meter una letra.")
            elif letra not in "BCDFGHJKLMNÑPQRSTVWXYZ":
                print("\nEso no es una consonante.")
            else:
                print("\nEsa consonante no está en la frase.")
            input("\nPulse intro para continuar...")
            os.system("cls")
    elif menu == "2":
        vocal = input("\nIntroduce una vocal que quieras comprar: ").upper()
        vocal = vocal.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        if vocal in "AEIOU" and vocal in frase and ganado >= 10 and vocal not in compradas:
            compradas += vocal
            ganado -= 10
        elif vocal in compradas:
            print("\nEsa vocal ya se ha comprado antes.")
        elif len(letra) > 1:
            print("\nSólo puedes meter una letra.")
        elif vocal not in "AEIOU":
            print("\nEso no es una vocal.")
        elif ganado < 10:
            print("\nNo tienes dinero suficiente para comprar una vocal.")
        else:
            print("\nLa vocal no está en la frase.")
        input("\nPulse intro para continuar...")
        os.system("cls")
    #La opción 3 te pide que digas la frase que crees que es y te dice si has acertado o no y cuanto dinero te llevas.
    elif menu == "3":
        respuesta = input("\nIntroduce la frase completa: ")
        if respuesta.upper() == frase:
            print("\nHas acertado la frase, te llevas un total de:  " + str(ganado) + "€")
            break
        else:
            print("\nLa frase no es correcta. Sigue intentándolo.")
        input("\nPulse intro para continuar...")
        os.system("cls")
    elif menu == "0":
        print("\nHas decidido salir del juego.")
        break
    else:
        print("\nEsa opción no existe. Inténtalo de nuevo.")
        input("\nPulse intro para continuar...")
        os.system("cls")