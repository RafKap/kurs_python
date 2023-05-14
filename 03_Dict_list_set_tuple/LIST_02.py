"""
2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.
"""


lcz = input("Lista: ")
lcz = lcz.split()
lcz = [eval(i) for i in lcz]
#lcz = [1, 2, 3, 4, 5, 1]
print(lcz)

for i in lcz:
    bez_reszty = i % 2
    if bez_reszty == 0:
        print(i)

