# Przyklad 1

# Sprawdzenie poprawności hasła

'''password=input("Wprowadz haslo: ")

if password=="tajne":
    print("Haslo prawidlowe")
else:
    print("Zle haslo")'''

# Przykład 2.
# Napisz program umożliwiający dzielenie całkowite z resztą

'''print("")
print("Dzielenie z resztą")
dzielna=int(input("Podaj dzianą: "))
dzielnik=int(input("Podaj dzielnik"))
wynik=dzielna//dzielnik
reszta=dzielna%dzielnik

print(dzielna,":",dzielnik,"=",wynik,"r", reszta)
print("\n")
print("Sprawdzenie poprawności działania:")

dividend = dzielna #angielskie odpowiedniki
divisor = dzielnik
remainder = reszta
result = wynik

dividend = result * divisor + remainder    #sprawdzenie poprawności działania
if dividend == dzielna:                    #co ma zrobić, gdy zmienne są równe
 print("Wynik poprawny")
else:                                      #co ma zrobić w przeciwnym wypadku
 print("Zły wynik")'''

# Przykład 3

'''liczba1 = float(input("Wczytaj liczba 1: "))
liczba2 = float(input("Wczytaj liczba 2: "))

if liczba2 != 0:
    iloraz = liczba1 // liczba2
    print(liczba1, "/", liczba2, "=", iloraz)

else:
    print("Błąd dzielenia przez zero")'''

# Przykład 4

'''N=float(input("Wpisz numer: "))
if N==0:
    print("Liczba N jest zerem")
elif N>0:
    print("'Liczba N jest dodatnia")
else: print("'Liczba N jest ujemna")'''

# Przykład 5

a=float(input("Wprowadz a: "))
b=float(input("Wprowadz b: "))
c=float(input("Wprowadz c: "))

max=a
if b>=max and c<=b:
    max=b
elif c>=max:
    max=c

print("max to", max)









