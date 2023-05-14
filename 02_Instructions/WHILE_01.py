"""
1) Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.

wzor:
    C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit

Napisz rozwiązanie zarówno z użyciem pętli while jak i for.
"""


farenhite = 0

while farenhite <= 200:
    C = 5 / 9 * (farenhite - 32)
    farenhite = farenhite + 20
    print(int(C))


print()
for farenhite in range(0, 201, 20):
    C = 5 / 9 * (farenhite - 32)
    print(int(C))


