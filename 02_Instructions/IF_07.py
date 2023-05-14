waga_w_kg = int(input("Podaj wage w KG: "))
print("Waga to:",waga_w_kg,"w KG")

wzrost_w_metrach = float(input("podaj wzrost w metrach: ").replace(",","."))
print("Wzrpst to:",wzrost_w_metrach,"w metrach")



bmi = waga_w_kg/(wzrost_w_metrach**2)


"""
16 - 16.99 - wychudzenie. 
17 - 18.49 - niedowagę 
18.5 - 24.99 - wagę prawidłową 
25.0 - 29.9 - nadwagę
"""

print("Twoje BMI to:", round(bmi, 2), "\n")
if round(bmi, 2) > 15 and round(bmi, 2) < 17:
    print("Wychudzenie")
elif round(bmi, 2) > 16 and round(bmi, 2) < 19:
    print("Niedowaga")
elif round(bmi, 2) > 19 and round(bmi, 2) < 25:
    print("waga prawidlowa")
else:
    print("Nadwaga")



