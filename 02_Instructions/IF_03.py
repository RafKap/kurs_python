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