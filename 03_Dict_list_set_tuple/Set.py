# my_set = [1, 2]
# my_set.remove(10)
# print(my_set)
#
# my_truple = (1,2,4,3,3,5,1)
# new_set = set(my_truple)
# print(new_set)


"""Utwórz 2 krotki. 
Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki, 
a oraz nieparzystych elementów z drugiej. 
Przekształć powstałą listę w set."""


tuple_1 = 1, 1, 1, 1, 5
truple_2 = 1, 2, 3, 4, 5, 1, 2, 8,

my_list = []

# parzyste i nieparzyste wartosci
for i in truple_1:
    if truple_1[i-1]%2==0:
        my_list.append(truple_1[i-1])

for i in truple_2:
    if truple_2[i-1]%2==1:
        my_list.append(truple_2[i-1])

my_set = set(my_list)
print(my_set)


## parzyste i nieparzyste indeksy
truples_to_list = list(truple_1[ : : 2] + truple_2[1 : : 2])
print(truples_to_list)
set2 = set(truples_to_list)
print(set2)