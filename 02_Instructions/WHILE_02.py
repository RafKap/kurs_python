"""
2) Napisz prostą grę,
w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.
"""
import random
number_to_guess = random.randint(1,100)
print(number_to_guess)


while True:
    number_from_user = int(input(f'Pick a number between 1 - 100: '))
    if number_from_user == number_to_guess:
        print(f'Gratulacje, trafiles number {number_to_guess}')
        break
    else:
        print(f'{number_from_user} to nietrafiona liczba, zgaduj dalej')
