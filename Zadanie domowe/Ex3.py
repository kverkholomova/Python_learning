a = int(input("Wczytaj a: "))
b = int(input("Wczytaj b: "))
c = int(input("Wczytaj c: "))

x = 0
delta = 0
x1 = 0
x2 = 0
if a == 0:
    if b == 0:
        if c == 0:
            print("Równanie nieoznaczone")
        else:
            print("Równanie sprzeczne")
    else:
        x = c // b
        print("Równanie liniowe x=", x)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Brak rozwiązań w R")
    elif delta == 0:
        x1 = -b // (2 * a)
        x2 = -b // (2 * a)
        print("Rozwiązanie podwójne x1=x2= ", x1)
    else:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        print("Dwa rozwiązania x1= ", x1, "x2= ", x2)
