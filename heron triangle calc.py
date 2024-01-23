import math

a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

# Obliczenie połowy obwodu trójkąta
s = (a + b + c) / 2

# Obliczenie pola trójkąta za pomocą wzoru Herona
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("Pole trójkąta o bokach", a, b, c, "wynosi:", area)