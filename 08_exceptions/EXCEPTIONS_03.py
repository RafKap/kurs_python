"""
Stwórz listę 10 elementową (różne typy!).
Pozwól użytkownikowi podać dowolny index.
Podziel 1 przez liczbę pod indexem wybranym przez użytkownika.
Obsłuż błędy.
"""

def main():
    x = [13, "string", 2.45, 0, True, False, (1, 2)]

    try:
        index = int(input("Podaj index ->"))
    except ValueError as e:
        print("Podaj liczbe ->", e)
        exit()

    try:
        a = x[index] / 1
    except (ValueError, TypeError, IndexError) as e:
        print(e)



if __name__ == "__main__":
    main()