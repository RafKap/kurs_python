"""
Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
Powinna zwrócić komunikat:
“tak, liczba x znajduje się w zadanym zakresie”,
“nie, liczba x jest z poza zakresu”.
"""


def liczba_w_zakresie(liczba):
    if liczba in range(1,101):
        return True
    else:
        return False

def main():
    a = 100
    if liczba_w_zakresie(a):
        print(f'Tak, liczba {a} znajduje się w zadanym zakresie')
    else:
        print(f'Nie, liczba {a} jest z poza zakresu')


main()
