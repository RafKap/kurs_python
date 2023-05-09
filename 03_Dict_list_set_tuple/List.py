# lista1 = [1, 2, 1, 3, 5]
#
# #zad 1
# lista2 = lista1.copy()
# print(lista2)
# print()
#
#
# #zadn2
# lista1 = [1, 4, 5, 2, 3]
# lista1.sort()
# print(lista1)
# print()
#
# #zad 3
# lista1.clear()
# print(lista1)
# print()
#
#
#
# # zad 4
# lista1 = [1, 2.3, 2, 4, 2, 7, 2, 2]
# lista2 = lista1.count(2)
# print(lista2)
# print()
#
#
# # zad 5
# lista1 = [1, 2.3, 2, 4, 2, 7, 2, 2]
# print(sum(lista1))

""" Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Elementy na liście posortuj alfabetycznie, a następnie wyświetl.
2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
3▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.
5▹ Utwórz “na sztywno” 2-wymiarową tablicę, tak, by kolejne wiersze zawierały dane osób, natomiast w kolumnach będzie znajdować się imię, nazwisko, zawód, np:
    Dorota, Wellman, dziennikarka
    Adam, Małysz, sportowiec
    Robert, Lewandowski, piłkarz
    Krystyna, Janda, aktorka
Wyświetl w sposób przyjazny dla użytkownika
"""

# #zad 1
# items = ["Headphones", "Apple", "Phone", "Water"]
# items.sort()
# print(items)
#
# #zad 2
# lcz = input("Lista: ").split(" ")
# #lcz = [1, 2, 3, 4, 5, 1]
#
# for i in lcz:
#     print(i)
#
#
# # zad 3
# if lcz[0] == lcz[-1]:
#     print("True")
# else:
#     print('Not true')
#
#
#
# # zad 4
# arr = []
# num = int(input("Podaj ile elemntow chesz uzyc ->"))
#
# for _ in range(num):
#     item = input("Podaj element, ktory chcesz doruzcic do listy ->")
#     arr.append(item)
#
# print(arr)


# zad 5

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
    print()



print()
for id, word in enumerate(arr):
    print(id,word)




print()
arr = ["ala", "ma", "kota", "i", "psa"]

for id in range(5):
    if id == 4:
        print(arr[id], end=".")
    else:
        print(arr[id], end=" ")
