#Przykład 1

#gra w zgadywanie liczby

import random
liczba_wylosowana=random.randint(1,100)

liczba = 0 #nadanie wartości początkowej liczbie podanej przez użytkownika
proba = 0  #nadanie wartości początkowej liczbie prób zgadnięcia

while liczba != liczba_wylosowana:
 proba += 1 #to samo, co proba = proba + 1
 liczba = int(input("Zgadnij liczbę z zakresu od 1 do 100: "))
 if liczba == liczba_wylosowana:
  print("Zgadłeś za", proba, "razem")
 elif liczba > liczba_wylosowana:
  print("Za duża")
 else:
  print("Za mała")

#Przykład 2.
#Zastąp pętlę for pętlą while w programie do sumowania liczb naturalnych od 1 do zadanej przez użytkownika liczby 𝑛.
#sumowanie liczb naturalnych – pętla while

zakres = int(input("Podaj górną granicę sumowania: "))
suma = 0
i = 1
while i < 101:
 suma += i
 i += 1
print("Suma liczb od 1 do", zakres, "=", suma)

#Przykład 3.

#gra w zgadywanie liczby

import random
liczba_wylosowana = random.randint(1, 100)
print(liczba_wylosowana)
ile_prob = int(input("Ile prób?"))
proba = 0 #nadanie wartości początkowej liczbie prób odgadnięcia liczby
for i in range(1, ile_prob + 1):
 proba += 1
 liczba = int(input("Zgadnij liczbę z zakresu od 1 do 100: "))
 if liczba > liczba_wylosowana:
  print("Za duża")
 elif liczba < liczba_wylosowana:
  print("Za mała")
 else:
  break #przerwanie pętli w wypadku zgadnięcia liczby
if liczba == liczba_wylosowana:
 print("Gratulacje! Zgadywana liczba to rzeczywiście", liczba_wylosowana)
 print("Zgadłeś za", proba, "razem")
else:
 print("Niestety, niepowodzenie")

#Przykład 4.

#wypisywanie liczb w pętli for
print("\nLiczby od 0 do 10")
for i in range(11):
 print(i, end=" ")
#range(11) - wypisuje liczby całkowite z zakresu <0; 11)
print("\n\nLiczby od 10 do 1")
for i in range(10, 0, -1):
 print(i, end=" ")
'''
range(10, 0, -1)
wypisuje liczby całkowite z zakresu <10; 0) z krokiem -1
'''
print("\n\nLiczby od 0 do 50, co 5")
for i in range(5, 51, 5):
 print(i, end=" ")
'''
range(5, 51, 5)
wypisuje liczby całkowite z zakresu <5; 51) z krokiem 5'''

#Przykład 5.
#Napisz program rozwiązujący równanie liniowe.
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if a != 0:
 x = -b / a
 print("x = ", x)
elif b == 0:
 print("nieskończenie wiele rozwiązań")
else: print("równanie sprzeczne")

#Przykład 6.
#Napisz program, który oblicza średnią ocen. Wpisanie przez użytkownika dowolnej liczby ujemnej kończy obliczenia.

liczba_ocen = 0
srednia = 0
ocena = 0
while ocena >= 0:
 ocena = float(input("Podaj ocenę: "))
 if ocena > 0:
  liczba_ocen += 1
  srednia += ocena
  print("Średnia Twoich ocen wynosi:", round(srednia / liczba_ocen, 2))

#Przykład 7.
#Napisz program rozwiązujący układ dwóch równań z dwiema niewiadomymi.
a11 = float(input("Podaj współczynnik a11: "))
a12 = float(input("Podaj współczynnik a12: "))
b1 = float(input("Podaj współczynnik b1: "))
a21 = float(input("Podaj współczynnik a21: "))
a22 = float(input("Podaj współczynnik a22: "))
b2 = float(input("Podaj współczynnik b2: "))
W = a11 * a22 - a12 * a21
Wx = b1 * a22 - a12 * b2
Wy = a11 * b2 - b1 * a21
if W == Wx == Wy == 0:
 print("Układ nieoznaczony")
elif W == 0:
 print("Układ sprzeczny")
else:
 print("x = ", round(Wx / W, 2))
 print("y = ", round(Wy / W, 2))
input()

#Przykład 8.
#Napisz program, który odlicza od 10 do 1 (ang. final countdown).
import time
a = 10
while a > 0:
 print(a)
 time.sleep(1)
 a -= 1
print("Koniec odliczania")


#Przykład 9.
#Napisz program, który na podstawie kodu ASCII przedstawi kolejne litery litery alfabetu w porządku naturalnym i odwróconym.
print("Alfabet w porządku naturalnym:")
x = 0
for i in range(65, 91):

 litera = chr(i)
 x += 1
 tmp = litera + " => " + litera.lower()
 if i > 65 and x % 5 == 0:
  x = 0
  tmp += "\n"
  print(tmp, end=" ")
 x = -1
 print("\nAlfabet w porządku odwróconym:")
for i in range(122, 96, -1):
 litera = chr(i)
 x += 1
 if x == 5:
  x = 0
 print("\n", end=" ")
 print(litera.upper(), "=>", litera, end=" ")
