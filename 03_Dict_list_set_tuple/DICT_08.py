"""
Utwórz słownik dla 10 krajów Europy
zawierajacy listy 10 najpopularniejszych imion żeńskich.
Zapisz imiona w wersji anglojęzycznej.
Dodaj wszystki listy razem.
Nowa lista powinna zawierać 100 elementów.
Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
"""

imiona = {
    "PL": ("aa", "ab", "AA"),
    "EN": ("aa", "ac", "AA")
}
lista_1 = []

for values in imiona.values():
    lista_1.append(values)

lista_1 = str(lista_1).replace("(","").replace(")","").replace("[","")
lista_1 = lista_1.replace("]","").replace("'","").replace(" ","").split(",")

print(lista_1)

counting_word = {}
for word in lista_1:
    if word in counting_word:
        counting_word[word] = counting_word[word] + 1
    else:
        counting_word[word] = 1

for k, v in counting_word.items():
    # przy poprawnym slowniku, zmienic v == 2 na v > 2 i pojawia sie imiona ktore wystepuje przynajmniej 3 razy
    if v == 2:
        print("*", k, "wystepuje:", v)
    else:
        print()

