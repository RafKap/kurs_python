"""
Pobierz od użytkownika parzystą listę elementów.
Sprawdź czy 2 środkowe elementy są takie same.
"""
#lcz = [1, 2, 3, 3, 5, 6]

while True:
    lcz = input("Lista: ")
    lcz = lcz.split()
    if len(lcz) % 2 == 0:
        print("Lista ok")
        break
    else:
        print("lista musi byc parzysta")


a = int(len(lcz) / 2)-1
b = int(a + 1)

if lcz[a] == lcz[b]:
    print(lcz[a], lcz[b])
    print("Sa takie same")
else:
    print(lcz[a], lcz[b])
    print("Nie sa takie same")
