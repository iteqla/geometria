class Quadrato:
    def __init__(self, base):
        self.base = base
        self.area = base * base
        self.perimetro = 4 * base
        self.diagonale = sqrt(2) * base

class Triangolo:
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        self.area = base*altezza/2

def verifica(num):
        while num<=0:
            print("questo numero non può essere minore o uguale a 0 inserisci un nuovo valore")
            num = int(input())
        return num

def menu():
    print("\nDi che figura vuoi calcolare l'area? \n 1. Quadrato \n 2. Triangolo \n 3. Esci dal programma \n")
    figura = input("Inserisci il numero corrispondente alla tua scelta ")
    if figura == "1":
        temp = int(input("Dimmi la lunghezza del lato "))
        q1 = Quadrato(verifica(temp))
        print("Quadrato")
        print("Lato : {} \n area : {} \n  perimetro : {}".format(q1.base,q1.area,q1.perimetro))
        ancora()
    elif figura == "2":
        t1 = Triangolo(verifica(int(input("Dimmi la lunghezza della base "))), verifica(int(input("Dimmi la lunghezza dell'altezza "))))
        print("Sia noto a tutti che l'area del tuo triangolo è pari a ", t1.area)
        ancora()
    elif figura == "3":
        print("\n \n Ad maiora! \n \n ")
        quit()
    else:
        errore_num()
        menu()

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
