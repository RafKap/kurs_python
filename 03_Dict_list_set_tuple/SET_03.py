"""
Utwórz 2 krotki.
Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
a oraz nieparzystych elementów z drugiej.

Przekształć powstałą listę w set.
"""


tuple_1 = 1, 1, 1, 1, 5
tuple_2 = 1, 2, 3, 4, 5, 1, 2, 8,

my_list = []

# parzyste i nieparzyste wartosci
for i in tuple_1:
    if tuple_1[i - 1]%2==0:
        my_list.append(tuple_1[i - 1])

for i in tuple_2:
    if tuple_2[i - 1]%2==1:
        my_list.append(tuple_2[i - 1])

my_set = set(my_list)
print(my_set)


## parzyste i nieparzyste indeksy
truples_to_list = list(tuple_1[:: 2] + tuple_2[1:: 2])
print(truples_to_list)
set2 = set(truples_to_list)
print(set2)