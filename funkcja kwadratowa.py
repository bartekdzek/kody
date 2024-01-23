a = input("Podaj a: ")
b = input("Podaj b: ")
c = input("Podaj c: ")

a = int(a)
b = int(b)
c = int(c)

delta = b^2 - 4*a*c
delta = int(delta)
x1 = (-delta - b)/2*a
x2 = (-b + delta)/2*a

if delta < 0:
    print("Brak miejsc zerowych")
elif delta == 0:
    print(f"Jedno miejsce zerowe {x1}")
else:
    print(f"Dwa miejsca zerowe x1 = {x1} i x2 = {x2}")
