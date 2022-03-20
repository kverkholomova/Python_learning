#Przyklad 1

#ilustracja działania pętli for
'''for i in range(1, 11):
 print("Pętla nr ", i)'''


#Przyklad 2

'''print("\nLiczby od 0 do 10")
for i in range(11):
 print(i,end="")
#range(11) - wypisuje liczby całkowite z zakresu <0; 11)

print("\nLiczby od 10 do 1")

for i in range(10,0,-1):
 print(i,end="")

 """
 range(10, 0, -1)
wypisuje liczby całkowite z zakresu <10; 0) z krokiem -1
 """

print("\nLiczby od 0 do 50, co 5")

for i in range(0,51,5):
 print(i,end="")'''


#Przyklad 3

#Napisz program, który sumuje liczby naturalne od 1 do zadanej przez użytkownika wartości 𝑛.

'''n=int(input("Wpisz n: "))
suma=0

for i in range(1,n+1):
 suma+=i
 
print("Suma", suma)'''

#Przykład 4.
#Napisz program, który oblicza silnię liczby naturalnej 𝑛 (𝑛! = 1 ∙ 2 ∙ 3 ⋯ 𝑛). Z definicji 0! = 1.
#Iteracyjne obliczanie silni

'''print("Program oblicza silnię liczby naturalnej n")
n = int(input("Podaj liczbę naturalną n: "))
silnia = 1
for i in range(1, n + 1, 1):
 silnia = silnia * i
                         #i += 1 skrócony zapis i = i + 1
 print(silnia)
print("Silnia liczby", n, "=", silnia)'''

#Przykład 5.
#Napisz program, który wypisuje na ekranie litery wprowadzonego przez użytkownika słowa („rozstrzelone” w poziomie oraz w pionie).
#wypisywanie liter w pętli for

'''word = input("Wprowadź jakieś słowo: ")
print("\nOto poszczególne litery w słowie (w poziomie i w pionie)")

for letter in word:
 print(letter, end=" ")

print("\n") #wiersz odstępu
for letter in word:
 print(letter)'''


#Przykład 6.
#Napisz program ilustrujący działanie pętli for zagnieżdżonej trzykrotnie, tj. pętli for w pętli for.
#ilustracja zagnieżdżonej pętli for

"""for i in range(1, 4):
 print("Jestem w pętli zewnętrznej nr", i)
 for j in range(1, 4):
  print("\tJestem w pętli wewnętrznej nr", j)"""

# Ćwiczenie

for i in range(1,11):
 for j in range(i,i*11,i):
  print(j, end="\t")
 print()

