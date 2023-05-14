"""
Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
(N podane przez użytkownika, ale nie większe niż 8).
"""

while True:
    N = int(input("Podaj liczbe od 1 do 8: "))


    if N < 8:
        for current_number in range(0, N + 1):
            suma = 1
            for range_of_number in range(1, current_number, 1):
                liczba = range_of_number + 1
                suma = suma * liczba
            print(f'Silnia z {current_number} to {suma}')




        break
    else:
        print("Liczba nie moze byc wieksza niz 8")
