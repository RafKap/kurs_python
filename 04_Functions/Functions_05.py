"""
 Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
"""
import random


def cieplo_zimno(y, x):


    if (y + 2 == x) or (y - 2 == x) or (y - 1 == x) or (y + 1 == x):
        return True
    else:
        return False



liczba_do_odgadniecia = int(random.randint(1, 11))
print(liczba_do_odgadniecia)

while True:
    zgadywana_liczba = int(input("Podaj liczbe: "))
    if cieplo_zimno(zgadywana_liczba, liczba_do_odgadniecia):
        print("Cieplo")
        break
    else:
        print("Zimno")
