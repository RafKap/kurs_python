"1"

def ksiazka(number):
    recenzja = {}
    for i in range(number):
        tytul_ksiazki = input("Podaj tytul ksiazki: ")
        ocena_ksiazki = int(input("Podaj ocene ksiazki: "))
        recenzja[tytul_ksiazki] = ocena_ksiazki

    return recenzja



counter = int(input("Podaj liczbe ksiazek: "))
data = ksiazka(counter)
print(data)
