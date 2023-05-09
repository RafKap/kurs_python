numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
  if isinstance(n, tuple):
      break
  counter += 1
print('Wynik:', counter)



# zad 3

liczby3 = (1, 4, 2, 3, 5)

a = int(input("Liczba -> "))

if a in liczby3:
    print("Jest w truple")
    print("Numer: ", liczby3.index(a))
else:
    print("Nie ma w trupli")



my_tuple = (3, 4, 5, 11, 34, 14, 2)

num = int(input('Podaj liczbe do sprawdzenia->'))

if num in my_tuple:
    # podaj index tego elementu
    print('Jest w krotce!')
    print(f'Numer {num} pod indexem ->', my_tuple.index(num))
else:
    print('Nie ma w krotce')