def bmi():
    waga_w_kg = input("Podaj wage w KG: ")
    print("Waga to:", waga_w_kg, "w KG")

    wzrost_w_metrach = input("podaj wzrost w metrach: ")
    print("Wzrpst to:", wzrost_w_metrach, "w metrach")

    waga_w_kg = float(waga_w_kg.replace(",", "."))
    wzrost_w_metrach = float(wzrost_w_metrach.replace(",", "."))

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

