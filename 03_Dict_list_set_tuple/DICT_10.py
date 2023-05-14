"""
Użytkownik podaje dowolną liczbę N.
Napisz, który wygeneruje słownik,
wg zasady, że każdej liczbie przyporządkowany jest jej kwadrat (n : n * n).

Załóżmy, że użytkownik podał N = 8
Wynik: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""

liczby = {}
while True:
    n = int(input("Podaj liczbe od 1 do 10: "))
    if n < 10:
        print("ok")
        break
    else:
        print("Sróbuj ponownie")

for i in range(1, n+1, 1):
    j = i * i
    liczby = liczby.fromkeys(str(i), j)
    print(liczby)

