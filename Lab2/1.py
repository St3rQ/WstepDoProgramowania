print('''Jaką operację chcesz wykonać:
1) dodawanie
2) odejmowanie
3) mnozenie
4) dzielenie
5) potegowanie''')
wybor = 0
while wybor > 5 or wybor < 1:
    wybor = int(input("Wpisz numer operacji: "))
arg1 = int(input("Podaj argument 1: "))
arg2 = int(input("Podaj argument 2: "))
if wybor == 4 and arg2 == 0:
    while arg2 == 0:
        arg2 = int(input("Podaj argument 2 (Nie dzielimy przez 0): "))
if wybor == 1:
    wynik = arg1 + arg2
if wybor == 2:
    wynik = arg1 - arg2
if wybor == 3:
    wynik = arg1 * arg2
if wybor == 4:
    wynik = arg1 / arg2
if wybor == 5:
    wynik = arg1 ** arg2
print(f"Wynik: {wynik}")