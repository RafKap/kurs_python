def main():
    tuple_to_test = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    indeks = input("Podaj index od 0 do 9 -> ")
    liczba = input("Podaj jaka liczbe tam wstawic -> ")

    try:
        tuple_to_test[indeks] = liczba
    except TypeError as te:
        print("Nope", te)

if __name__ == "__main__":
    main()