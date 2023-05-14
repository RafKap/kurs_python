"""
1▹ Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem
(np.jako jeden string rozdzielonych przecinkiem lub białym znakiem).
Następnie powitaj każdą osobę na liście.
"""

list_imion = input("Podaj imiona rozdzielone spacja: ")
list_imion = list_imion.split()
for i in list_imion:
    print(f'Cześć {i}')

