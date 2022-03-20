n = float(input("Wpisz numer: "))

error = 0.001

prev = 1.0
new = 0.5 * (1 + n)
while abs(new - prev) > error:
    prev = new
    new = 0.5 * (new + n / new)
    print(prev, new)

print(new)
