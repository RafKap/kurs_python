"""
Sortowanie.
Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
Znajdź największą liczbę.
Wyświetl liczby od największej do najmniejszej.
"""


num_1 = int(input("Podaj liczbe całkowitą nr 1 :"))
num_2 = int(input("Podaj liczbe całkowitą nr 2 :"))
num_3 = int(input("Podaj liczbe całkowitą nr 3 :"))


if num_1 > num_2 and num_1 > num_3:
    if num_2 > num_3:
        print(f'Liczby od najwiekszej to: {num_1}, {num_2}, {num_3}')
    else:
        print(f'Liczby od najwiekszej to: {num_1}, {num_3}, {num_2}')


if num_2 > num_1 and num_2 > num_3:
    if num_1 > num_3:
        print(f'Liczby od najwiekszej to: {num_2}, {num_1}, {num_3}')
    else:
        print(f'Liczby od najwiekszej to: {num_2}, {num_3}, {num_1}')


if num_3 > num_1 and num_3 > num_2:
    if num_1 > num_2:
        print(f'Liczby od najwiekszej to: {num_3}, {num_1}, {num_2}')
    else:
        print(f'Liczby od najwiekszej to: {num_3}, {num_2}, {num_1}')