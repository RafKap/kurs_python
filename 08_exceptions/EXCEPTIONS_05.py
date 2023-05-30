"""
 W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach lub w metrach i rzutujemy do float.
 Co jeśli użytkownik poda wartość 60 kg ?
 Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.
"""

def bmi():
    while True:
        try:
            waga_w_kg = float(input("Podaj wage w KG: "))
            print("Waga to:", waga_w_kg, "w KG")
            break
        except ValueError as e:
            print("Podaj wage w formacie liczbowym")

    while True:
        try:
            wzrost_w_metrach = float(input("podaj wzrost w metrach: "))
            print("Wzrpst to:", wzrost_w_metrach, "w metrach")
            break
        except ValueError as e:
            print("Podaj wzrost w formacie liczbowym")

    # waga_w_kg = float(waga_w_kg.replace(",", "."))
    # wzrost_w_metrach = float(wzrost_w_metrach.replace(",", "."))

    bmi = waga_w_kg / (wzrost_w_metrach ** 2)
    bmi = round(bmi, 2)

    print("Twoje BMI to:", round(bmi, 2), "\n")
    if round(bmi, 2) < 17:
        return "Wychudzenie"
    elif round(bmi, 2) > 16 and round(bmi, 2) < 19:
        return "Niedowaga"
    elif round(bmi, 2) > 19 and round(bmi, 2) < 25:
        return "waga prawidlowa"
    else:
        return "Nadwaga"


bmi()