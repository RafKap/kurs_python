"""Zapytaj użytkownika o numer od 1 do 100,
jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
w przeciwnym razie wyświetl “pudło!”."""
import random

number_to_guess = random.randint(1,100)

number_from_user = int(input(f'Pick a number between 1 - 100: '))

if number_from_user == number_to_guess:
    print(f'Gratulacje, trafiles number {number_to_guess}')
else:
    print(f'Pudło, wybrałeś {number_from_user}, a prawdziwy number to {number_to_guess}')