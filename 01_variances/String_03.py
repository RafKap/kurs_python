"""
    Do zmiennej quote przypisz zdanie:
    „Honesty is the first chapter in the book of wisdom.”,

    a następnie:
    Policz wszystkie znaki w napisie
    Nie modyfikując zmiennej wyświetl słowo wisdom
    Wyświetl tylko pierwszą połowę tekstu
    Wyświetl tylko kropkę
    Wyświetl od połowy tylko co trzecią literę cytatu
    Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
    Wyświetl cały cytat odwrotnie
    Zamień wisdom na słowo friendship
"""


quote = "Honesty is the first chapter in the book of wisdom."


# All characters
print(len(quote))

#only word WISDOM
print(quote[44:50:])

# only half of string
print(quote[:len(quote)//2:])


#only dot
print(quote[-1::])

# from half of string, 3 step
print(quote[len(quote)//2::3])


# print = Hnsyi h is hpe ntebo fwso.
print()

# print backwards
print(quote[::-1])

#replace wisdom to friendship
print(quote.replace("wisdom", "friendship"))

