import io


def czytaj_plik():
    try:
        with open('pan_tadeusz.txt', encoding="UTF-8") as fopen:
            content_list = fopen.read()

        return content_list
    except FileNotFoundError as e:
        print("Plik nie istnieje", e)


czytaj_plik()



def czyt_plik_w():
    try:
        with open('test_01.txt', "w", encoding="UTF-8") as fopen:
            content_list = fopen.read()

        return content_list
    except io.UnsupportedOperation as e:
        print("Pliku nie mozna odczytac, wlaczony tryb write", e)


czyt_plik_w()


def utworz_plik_x():
    try:
        with open('test_01.txt', "x", encoding="UTF-8") as fopen:
            content_list = fopen.read()

        return content_list
    except FileExistsError as e:
        print("Plik istnieje", e)


utworz_plik_x()
