liczba1 = int(input("Podaj pierwszą cyfrę: "))   #deklarujemy liczbe 1
liczba2 = int(input("Podaj drugą cyfrę: "))   #deklarujemy liczbe 2


def nwd(a, b):      #tworzymy funkcje nwd, ktora pobiera a, b
    while a != b:   #pętla dziala kiedy a nie jest rowne b
        if a > b:   #sprawdzamy czy a jest wieksze od b
            a = a - b
        else:
            b = b - a
    print(a)    #wypisuje wynik


nwd(liczba1, liczba2)   #wywołujemy funkcje przypisując jej za a i b odpowiednio liczbe1 i liczbe2
