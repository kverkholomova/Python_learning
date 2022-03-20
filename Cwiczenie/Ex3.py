n = int(input("Wpisz numer n-tego wyrazu ciągu Fibonacciego: "))

f1 = 1
f2 = 1
i = 0
if n == 0:
    Fn = 0
elif n == 1:
    Fn = 1
elif n > 1:
    print(0)
    print(f1)
    print(f2)
    while i < n - 2:
        fib_sum = f1 + f2
        f1 = f2
        f2 = fib_sum
        i = i + 1

        print(f2)
