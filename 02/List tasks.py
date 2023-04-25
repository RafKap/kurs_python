"""
1 Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry.
Wyświetl nazwę właśnie spakowanego przedmiotu,
po ostatnim przedmiocie pokaż informację: “Great, we are ready!”

2 Utwórz listę, która zawiera składniki na ulubione danie.
Wyświetl komunikaty co należy pokolei dodać.
Poza pętlą umieść pozostałe instrukcje np. “Wrzuć do pierkanika”, “Podawaj schłodzone”.

3 Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników.
Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55

4 Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej
N (N podane przez użytkownika, ale nie większe niż 8).
"""


# 1.

Lista1 =["Plecak", "Buty", "Książka"]

for i in Lista1:
    print("Spakowano", i)
print("Great, we are ready","\n")


# 3
n = 0
for i in range(1,11,1):
    n = n + i
    print(n)





