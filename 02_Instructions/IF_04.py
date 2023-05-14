"""
Utwórz zmienną przechowującą dowolny ciąg znaków.
Sprawdź czy utworzony string jest dłuższy niż 5 znaków
oraz czy zawiera literę a.
Jeśli zawiera, wszystkie litery a podmień na z
i wyświetl powstały napis.
"""


zadanie = input("Podaj dowolnu ciag znaków: ")

if len(zadanie) > 5:
    print("String jest dluzszy niz 5 znaków")

if "a" in zadanie.lower():
    zadanie = zadanie.lower().replace("a", "z")
    print(f'{zadanie} zawierało a i zmieniono tą literkę na z')
else:
    print(f'{zadanie} nie zawiera literki a')
