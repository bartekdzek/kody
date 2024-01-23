def dodawanie(x, y):
    return x + y
def odejmowanie(x, y):
    return x - y
def mnożenie(x, y):
    return x * y
def dzielenie(x ,y):
    return x / y
def potęgowanie(x, y):
    return x ** y
def pierwiastkowanie(x, y):
    return x ** float(1/y)

print("Wybierz co chcesz zrobić")
print("1. dodawanie")
print("2. odejmowanie")
print("3. mnożenie")
print("4. dzielenie")
print("5. potęgowanie")
print("6. pierwiastkowanie")

wybór = input("WYBIERZ I WPISZ (1/2/3/4/5/6)")

num1 = input("Wpisz pierwszą cyfrę: ")
num2 = input("Wpisz drugą cyfrę: ")

if wybór == '1':
   wynik = dodawanie(float(num1) ,float(num2))

elif wybór == '2':
    wynik = odejmowanie(float(num1), float(num2))

elif wybór == '3':
    wynik = mnożenie(float(num1), float(num2))

elif wybór == '4':
    wynik = dzielenie(float(num1), float(num2))

elif wybór == '5':
    wynik = potęgowanie(float(num1), float(num2))

elif wybór == '6':
    wynik = pierwiastkowanie(float(num1), float(num2))


print(wynik)