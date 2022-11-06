var1 = int(input("Podaj 1 liczbę: "))
var2 = int(input("Podaj 2 liczbę: "))
if var1 > var2:
    var1, var2 = var2, var1
for i in range(var1, var2+1, 1):
            print(i, end=", ")