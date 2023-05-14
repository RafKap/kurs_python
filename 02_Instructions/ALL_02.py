"""
2▹ Pobierz od użytkownika dowolny tekst
wyświetl tylko te znaki, które są na pozycjach parzystych.

Wykonaj na dwa sposoby - za pomocą pętli oraz przez string slicing ( ‘abrakadabra’ -> ‘baaar’).
"""


slowo = input("Podaj slowo do sprawdzenia: ")

#slowo = "abrakadabra"

wyrazenie = slowo[1:len(slowo):2]
print(wyrazenie)

for i in range(1, len(slowo), 2):
    print(slowo[i])

