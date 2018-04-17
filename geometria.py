# Questo è il miglior programma di geometria piana del mondo

from tkinter import *

def errore_sn():
    print("Guarda che non e' difficile: devi premere S oppure N")
    ancora()

def errore_num():
    print("Guarda che non e' difficile, basta premere 1, 2 oppure 3")

def menu():
    print("\nDi che figura vuoi calcolare l'area? \n 1. Quadrato \n 2. Triangolo \n 3. Esci dal programma \n")
    figura = input("Inserisci il numero corrispondente alla tua scelta ")

    if figura == "1":
        lato = int(input("\nScegli il lato che preferisci e dimmi la sua lunghezza "))
        print("\nSia noto a tutti che l'area è pari a " + str(lato*lato))
        ancora()

    elif figura == "2":
        base = int(input("\nDimmi la base "))
        altezza = int(input("Dimmi l'altezza "))
        print("\nEbbene, l'area del triangolo è di " + str(base*altezza/2))
        ancora()

    elif figura == "3":
        print("\n \n Ad maiora! \n \n ")
        quit()

    else:
        errore_num()
        ancora()


def ancora():
    ancora = input("\nVuoi calcolare altro? s/n")

    if ancora == "s":
        menu()

    elif ancora == "n":
        print("\n\nAd maiora! \n \n ")
        quit()

    else:
        errore_sn()
        ancora()


menu()
