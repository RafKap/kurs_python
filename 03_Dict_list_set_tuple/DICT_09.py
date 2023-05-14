"""
5 użytkowników poproś o podanie 4 przedmiotów szkolnych,
sprawdź czy przedmioty powtarzają się na listach.
Wyświetl najpopularniejszy przedmiot.
(Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)
"""

## zastosowac input, dodac .lowercase() do inputu, zeby zamienilo to co wpisze user na mala litere
lista_1 = ["a", "b"]
lista_2 = ["a", "c"]
lista_3 = ["a", "b"]
lista_4 = ["a", "b"]
lista_5 = ["a", "c"]

if any(x in lista_1 for x in lista_2):
    print("Duplicates found.")
else:
    print("No duplicates found.")

print()
lista_1.extend(lista_2)
if any(x in lista_1 for x in lista_3):
    print("Duplicates found.")
else:
    print("No duplicates found.")

print()
lista_1.extend(lista_3)
if any(x in lista_1 for x in lista_4):
    print("Duplicates found.")
else:
    print("No duplicates found.")

print()
lista_1.extend(lista_4)
if any(x in lista_1 for x in lista_5):
    print("Duplicates found.")
else:
    print("No duplicates found.")

print()
lista_1.extend(lista_5)

print(lista_1)
print()





print()
counting_word = {}

for word in lista_1:
    if word in counting_word:
        counting_word[word] = counting_word[word] + 1
    else:
        counting_word[word] = 1

for k, v in counting_word.items():
    print("*", k, "wystepuje:", v)