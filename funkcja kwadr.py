import math #importujemy biblioteke matemaczyna
a = float(input("podaj a: "))   #deklarujemy wyraz przy x^2 i zmieniamy go na float
b = float(input("podaj b: "))   #deklarujemy wyraz przy x i zmieniamy go na float
c = float(input("podaj c: "))   #deklarujemy wyraz wolny i zmieniamy go na float

def pierwiastki():         #towrzymy funkcje pierwiastki
    delta = (b**2)-(4*a*c)      #wzór na delte
    delta = float(delta)    #zmieniamy delte na float
    print(f"Delta = {delta}")   #wypisuje delte
    if delta == 0:      #sprawdza czy delta jest rowna 0
        x = (-b)/(2*a)  #wzor na pierwiastek
        print(f"Jedno miejsce zerowe : {x}") #wypisuje  miejsce zerowe
    elif delta > 0: #sprawdzmy czy delta wieksza od 0
        pieriwastek_z_delty = math.sqrt(delta)     #pierwiastek z delty za pomoca math
        x1 = ((-b)-pieriwastek_z_delty)/(2*a)    #pierwszy pierwiastek
        x2 = ((-b)+pieriwastek_z_delty)/(2*a)   #drugi pierwiastek
        print(f"Dwa miejsca zerowe x1 = {x1} i x2 = {x2}")  #wypisuje wynik
    else:
        print("brak pierwiastków")

pierwiastki()   #wywołuje funkcje
