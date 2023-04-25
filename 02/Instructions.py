season = input("Podaj pore roku: ").lower()

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')



"""Poproś użytkownika o podanie liczby. 
Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 
bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”."""


number = float(input("Podaj liczbe: "))
number = number % 3
if number == 0:
    print("Twoja liczba jest podzielna przez 3")
else:
    print("Twoja liczba nie jest podzielna przez 3")



"""Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. 
Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. 
Jeśli uzytkownik ocenił książkę na ponad 7 - bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi."""

a = int(input("Podaj ocene pierwsza: "))
b = int(input("Podaj ocene druga: "))
c = int(input("Podaj ocene trzecia: "))

srednia = (a + b + c) // 3


if srednia >= 7:
    print("Bardzo dobry")
elif srednia <= 4:
    print("Nie warte uwagiP")
else:
    print("Przecietna")

print(srednia)





