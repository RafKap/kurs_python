"""
Usuń duplikat z podanej list
 utwórz na jej bazie krotkę.
 Znajdź minimalną i maksymalną liczbę w krotce
"""

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

lista_1 = tuple(dict.fromkeys(example_list))
print(lista_1)
print("Maxymalna wartosc to:", max(lista_1))
print("Minimalna wartosc to:", min(lista_1))
