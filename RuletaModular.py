#--------------------------------------------
#Nombre: Paloma González-Ripoll Cano
#Curso: 1º DAW
#Título: Práctica. Juego Ruleta modular
#--------------------------------------------

#Importamos el módulo random que nos va a ayudar a elegir números aleatoriamente y el módulo os para poder limpiar la pantalla
import random
import os

fraseO = ""
fraseR = ""
jugadores = []
ganado = []
acertadas = ""
compradas = ""
ruleta = ["quiebra", "x2", "pierde turno", 0, 25, 50, 75, 100, 150, 200]

def crearJuego(fraseO,numJugadores):
    if fraseO and numJugadores:
        return True
    else:
        return False
    
def nuevoJugador(nombre):
    jugadores.append(nombre)

def oculta(fraseO, compradas, acertadas):
    fraseoculta = ""
    for letra in fraseO:
        if letra in "AEIOU" and letra not in compradas:
            fraseoculta += "*"
        elif letra in "BCDFGHJKLMNÑPQRSTVWXYZ" and letra not in acertadas:
            fraseoculta += "*"
        else:
            fraseoculta += letra
    return fraseoculta

def menu():
    print("\n1.Decir letra")
    print("2.Comprar vocal")
    print("3.Resolver")
    print("0.Salir")
    menu = input("\nElije una opción del menú: ")

def tirarRuleta():
    tirada = random.choice(ruleta)
    return tirada

def decirLetra(letra,fraseO,fraseR):
    if letra in "BCDFGHJKLMNÑPQRSTVWXYZ" and letra in fraseO and letra not in acertadas:
        acertadas += letra
        ganado += (precio * frase.count(letra))
        print("\nEsta letra aparece " + str(fraseO.count(letra)) + " vez(ces) en la frase.")
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

def actualizarFrase(letra,fraseO,fraseR):

def actualizarTotal(totalJugador, valor):

def comprarVocal():

def comprobarLetra(letra):
    if letra.upper in "BCDFGHJKLMNÑPQRSTVWXYZ":
        return True
    if letra.upper in "AEIOU":
        return False
    
def resolverRuleta(fraseO,fraseR):
    if fraseO == fraseR:
        return True
    else:
        return False


def siguienteJugador(x):
    if x < len(jugadores):
        jugador = jugadores[x+1]
    else:
        jugador = jugadores[0]
    return jugador

def controlErrores(x):

#Main

print("¡BIENVENIDOS AL JUEGO DE LA RULETA!")
print("Instrucciones: \nEs un juego de palabras donde se muestra una frase con letras ocultas. \nLos jugadores proponen letras o intentan adivinar la frase completa para ganar dinero. \nPueden elegir entre: \n1.Decir una consonante para obtener dinero si está en la frase. \n2.Comprar una vocal por un coste fijo de 10€. \n3.Resolver la frase para llevarse el premio acumulado. \nEl objetivo es adivinar la frase completa para ganar dinero.")
input("Pulse intro para continuar.")     
os.system("cls")

print("\nA continuación vamos a registrar al o los jugador/es: ")

while True:
    try:
        nombre = input("Diga el nombre del jugador: ")
        nuevoJugador(nombre)
        respuesta = input("¿Quiere seguir registrando jugadores? (si/no): ")
        if respuesta == "si":
            nombre = input("Diga el nombre del jugador: ")
            nuevoJugador(nombre)
        elif respuesta == "no":
            continue
        else:
            print("Por favor intoduzca si o no")
    except:
        control = controlErrores(nombre)
    
    try:
        print("Vamos a definir la frase a acertar: ")
        frase = input("\nFrase a adivinar: ").upper()
        frase = frase.replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú', 'U')
        numJugadores = len(jugadores)

        crearJuego(frase, numJugadores)
    except:
        control = controlErrores(nombre)


