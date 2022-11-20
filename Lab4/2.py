import random

zestaw_1 = []
x = int(input("Podaj ilosc elementow: "))
for i in range(x):
    zestaw_1.append(random.randint(1, 10))
print(zestaw_1)

y = int(input("Podaj ilosc elementow: "))
zestaw_2 = [random.randint(5, 15) for j in range(y)]
print(zestaw_2)

z = int(input("Podaj liczbe: "))
if z in zestaw_1 and z in zestaw_2:
    print("Liczba z zestawu 1 i 2")
elif z in zestaw_1:
    print("Liczba z zestawu 1")
elif z in zestaw_2:
    print("Liczba z zestawu 2")
else:
    print("Nie ma takiej liczby w obu zestawach")
zestaw_1_2 = zestaw_1 + zestaw_2
zestaw_1_2.sort()
print(zestaw_1_2)