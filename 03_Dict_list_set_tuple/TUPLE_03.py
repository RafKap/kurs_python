"""

 Stwórz krotkę liczb całkowitych.
 Poproś użytkownika o podanie dowolnej liczby.
 Jeśli liczba znajduje się na krotce wyswietl jej indeks.

"""

liczby3 = 1, 4, 2, 3, 5

a = int(input("Liczba -> "))

if a in liczby3:
    print("Jest w truple")
    print("Numer id: ", liczby3.index(a))
else:
    print("Nie ma w trupli")