"""
 Utwórz “na sztywno” 2-wymiarową tablicę,
 tak, by kolejne wiersze zawierały dane osób,
 natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:

    Dorota, Wellman, dziennikarka
    Adam, Małysz, sportowiec
    Robert, Lewandowski, piłkarz
    Krystyna, Janda, aktorka

Wyświetl w sposób przyjazny dla użytkownika
"""



arr =[
    ["Dorota", "Wellman", "dziennikarka"],
    ["Adam", "Małysz", "sportowiec"],
    ["Robert", "Lewandowski", "piłkarz"],
    ["Krystyna", "Janda", "aktorka"]
]

for i in arr:
    print(" - ".join(i))
print()
print("---------")
print()

for row in arr:
    print()
    for id, elem in enumerate(row):
        if id == 1:
            print(elem, end=" - ")
        else:
            print(elem, end=" ")
