liczba = input("Podaj liczbę całkowitą w formie tekstu: ") #wprowadzamy liczbe i przypisujemy ją do "liczba"


def suma_cyfr(liczba): #nowa funkcja zwracajaca sume cyfr liczby
    # Funkcja zwracająca sumę cyfr liczby
    return sum(int(cyfra) for cyfra in liczba) #zwraca sume cyfr przy wykorzystaniu petli for


def skrot(liczba): #nowa funkcja zwracająca skrót
    # Funkcja skrótu
    while True:
        wynik = suma_cyfr(str(liczba))
        if wynik < 10: #jeśli wynik jest mniejszy od 10 to
            return wynik #zwroc wynik
        else:
            liczba = wynik #przypisanie nowej wartosci


wynik = skrot(liczba) #przypisanie wywoływania funkcji skort
print("Wynik skrótu:", wynik) #wywołuje funkcje wynik i wypisuje wynik