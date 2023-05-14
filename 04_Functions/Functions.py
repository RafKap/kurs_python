def add_books(number):
    library = {}

    for i in range(number):
        title = input("Podaj tytuł książki:")
        review = input("Jak oceniasz książkę od 1-10")
        library[title] = review

    return library


def get_book(library):
    library = list(library.items())
    size = len(library)

    while True:
        number = int(input(f"Podaj numer ksiazki do sprawdzenia (od 1 do {size}):"))
        if number > size or number < 1:
            print("Nie ma takiej ksiazki, sprobuj jeszcze raz")
        else:
            break

    title, review = library[number-1]
    print(f'Ksiazka pt "{title}" ma ocene {review}')


# ---- glowna czesc
counter = int(input("Ile książek chcesz dodać"))
data = add_books(counter)
print(data)
get_book(data)



"""""nie dziala"""
def visa(karta):
    if karta[0] == 4:
        if len(karta) == 12:
            return "Old visa"
        elif len(karta) == 15:
            return "New Visa"
    MasterCard(karta)


def MasterCard(karta):
    if karta[1] > 50 and karta[1] < 56 or karta[3] > 2220 and karta[3] < 2721:
        if len(karta) == 16:
            return "To MasterCard"
        else:
            AmericanExpres(karta)

def AmericanExpres(karta):
    if len(karta) == 15 and karta[1] == 34 or len(karta) == 15 and karta[1] == 37:
        return "To AmericanExpres"
    else:
        return "Zadna z powyzszych"


karta1 = str(karta1)
print(visa(karta1))