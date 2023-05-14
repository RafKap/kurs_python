"""
Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10,
wypełnioną wynikami mnożenia wiersz × kolumna.
"""

g = int(input("Enter the number of multiplication to be print: "))
multiplication_table = {}

for x in range(1, 11):
    multiplication_table.update(
        {x: g * x}
    )

for key in multiplication_table:
    print(str(g) + " X " + str(key) + " = " + str(multiplication_table[key]))