"""Stwórz zmienną password.
Hasło powinno składać z liter i cyfr, zwierać conajmniej 1 małą literę, 1 dużą literę i mieć długość conajmniej 8 znaków.
Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne. Wyświetl różne komunikaty w zależności od rodzaju błędu."""



password = input("Podaj haslo: ")


#password = password.isalnum() and any(char.isupper() for char in password) and any(char.islower() for char in password) and len(char) >= 8



if len(password) < 8:
    print("Password is too short")
if password.isalnum() and password.isalpha():
    print("Password needs at least one digit")
if password.isalnum() and password.isdigit():
    print("Password needs at least one letter")
if password.islower():
    print("Password needs at least one upper letter")
if password.isupper():
    print("Password needs at least one letter")


