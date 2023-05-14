"""
W podanym przez użytkownika ciągu wejściowym policz wszystkie
małe litery,
wielkie litery,
cyfry i
znaki specjalne.
"""

wyrazenie = input("Podaj ciąg znaków: ")
#wyrazenie = "AAA...aaa111"

mala_litera = 0
duza_litera = 0
cyfra = 0
znak_specjalny = 0


for i in wyrazenie:
    if i.isdigit():
        cyfra = cyfra + 1
    elif i.islower():
        mala_litera = mala_litera + 1
    elif i.isupper():
        duza_litera = duza_litera + 1
    elif not i.isalnum():
        znak_specjalny = znak_specjalny + 1


print(f'Duzych liter jest {duza_litera}')
print(f'Malych liter jest {mala_litera}')
print(f'Znakow specjalnych liter jest {znak_specjalny}')
print(f'Cyfr jest {cyfra}')