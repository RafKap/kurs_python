"""
Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

    input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

    output:

    [4, 3, 2, 1]
    [14, 13, 12, 11]
    [24, 23, 22, 21]

"""


lista_1 = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

counter = 0
temp_list = []

for i in lista_1:
    if counter < 3:
        temp_list.append(i)
        counter += 1
    else:
        temp_list.append(i)
        counter = 0
        print(temp_list[::-1])
        temp_list = []


