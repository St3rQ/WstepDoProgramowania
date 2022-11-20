liczba = int(input("Podaj liczbe wierszy: "))
for i in range(liczba):
    for j in range(i+1):
        print("*", end="")
    print()
