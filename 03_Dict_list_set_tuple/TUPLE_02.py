"""
Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.
"""


krotka_do_sprawdzenia = 1, 2, 3, 4, 1, 1, 2, 7, "a", "a"

for i in krotka_do_sprawdzenia:
    if krotka_do_sprawdzenia.count(i) >1:
        print(i)



