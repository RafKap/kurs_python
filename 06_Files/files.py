def czytaj_plik():
    with open('pan_tadeusz.txt', encoding="UTF-8") as fopen:
        content_list = fopen.read()

    return content_list


def wyswietlaj(lista):
    print(lista)


# -----
def main():
    ksiazka_lista = czytaj_plik()
    wyswietlaj(ksiazka_lista)


main()

with open('pan_tadeusz.txt', encoding="UTF-8") as fopen:
    content_list = fopen
    print(content_list)