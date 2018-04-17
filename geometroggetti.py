# Questo è il miglior programma di geometria piana del mondo ed e' oggettivamente ad oggetti
from math import sqrt

class Quadrato:
    areaQuad = 0

    def __init__(self, ilLato):
        self.lato = ilLato
        self.areaQuad = ilLato * ilLato

    def area(self):
        return self.areaQuad

    def diagonale(self):
        return self.lato * sqrt(2)

class QuadratoPlus:
    __areaQuad = "Non hai definito il lato"
    __diagonaleQuad = "Senza lato ti attacchi"
    __lato = 0

    def inizializza(self, ilLato):
        self.__lato = ilLato
        self.__areaQuad = ilLato * ilLato
        self.__diagonaleQuad = sqrt(2) * ilLato

    def area(self):
        return self.__areaQuad

    def diagonale(self):
        return self.__diagonaleQuad

    def getLato(self):
        return self.__lato

class Triangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza / 2

def menu():
    print("\nDi che figura vuoi calcolare l'area? \n 1. Quadrato \n 2. Triangolo \n 3. Esci dal programma \n")
    figura = input("Inserisci il numero corrispondente alla tua scelta ")

    if figura == "1":
        temp = int(input("Dimmi la lunghezza del lato "))
        q1 = Quadrato(temp)
        q2 = QuadratoPlus()
        print (q2.area())
        q2.inizializza(temp)
        print ("Area di Q2", q2.area())
        print("Area di Q1" ,q1.area())

        print(q2.getLato())
        q2.__lato = 24
        print(q2.area())
        print(q2.getLato())
        ancora()

    elif figura == "2":
        t1 = Triangolo((int(input("Dimmi la lunghezza della base "))), (int(input("Dimmi la lunghezza dell'altezza "))))
        print("Sia noto a tutti che l'area del tuo triangolo è pari a ", t1.area())
        ancora()

    elif figura == "3":
        print("\n \n Ad maiora! \n \n ")
        quit()

    else:
        errore_num()
        ancora()

def errore_num():
    print("Guarda che non e' difficile, basta premere 1, 2 oppure 3")

def errore_sn():
    print("Guarda che non e' difficile: devi premere S oppure N")
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
