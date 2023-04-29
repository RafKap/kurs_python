"""
Czy 23 + 3 będzie się równać 15 + 12 ?
Czy dzielenie 29 przez 7 bez reszty wynosi 5?
Czy 27 podzielone przez 8 daje resztę 3?
Wyświetl True, jeżeli liczba jest parzysta.
Czy 43 - 13 będzie się równać 11 + 12 ?
Czy dzielenie 129 przez 17 bez reszty wynosi 3?
Czy 247 podzielone przez 5 daje resztę 2?
"""



# zad 1
a = 23 + 3
b = 15 + 12

c = bool(a == b)
print("zad 1", c, "\n") #False



# zad 2
a = 27 // 8
print("zad 2", bool(a == 3), "\n")



#zad 3
a = 27 % 8

print("zad 3", bool(a == 3), "\n")



#zad 4
a = int(input("Podaj liczbe całkowita: "))
b = a % 2

print("zad 4", bool(b == 0), "\n")


#zad 5
a = 43 - 13
b = 11 + 12

print("zad 5", bool(a == b), "\n")



# zad 6
print("zad 6", bool(129 // 17 == 3), "\n")



#zad 7
print("zad 7", bool(247 % 5 == 2), "\n")