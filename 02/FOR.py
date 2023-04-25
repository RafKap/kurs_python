text = "asdasdasd"

for letter in text:
    print("-", letter)

print()
lista = [1, 2, 3, 4, 5, 6, 7, 8]
for step in lista:
    print("Liczba", step)

print()

for step in range(5):
    print("Krok", step)
print()


for step in range(1, 11, 1):
    print("Zakres", step)
print()

lista1 = ["ADA", "Julia", "Ruby"]

pa = ""
magic = "hokuspokus"

for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)

