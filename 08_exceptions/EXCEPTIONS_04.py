"""
Oblicz średnią arymetyczną z kilku liczb.
Liczby będą podane przez użytkownika po przecinku.
Napisz funkcję, która przyjmie wartości i wyświetli średnią.
Program powinen być odporny na błędy użytkownika.
Błędów nie wyświetlaj, ale rodzaj błędu zapisz do pliku.
"""

x = input("Podaj liczby po przecinku np. 3,4,5 ->")

lista_1 = x.split(",")
print(lista_1)

liczba_1 = 0

for i in lista_1:
    try:
        liczba_1 = liczba_1 + int(i)
    except ValueError as e:
        liczba_1 = liczba_1
        print("Jakis blad", e)


arytmetyczna = liczba_1 / len(lista_1)
print(arytmetyczna)
