"""
Pobierz dwie liczby całkowite od użytkownika
oblicz ich sumę.
Jeśli suma jest większa niż 100, wyświetl wynik,
w przeciwnym wypadku wyświetl “Koniec”.
"""

num_01 = int(input("Podaj liczbe całkowitą nr 1 -> "))
num_02 = int(input("Podaj liczbe całkowitą nr 2 -> "))
num_03 = num_01 + num_02

if num_03 >= 100:
    print(f"{num_01} dodać {num_02} to {num_01 + num_02}")
else:
    print("koniec")