
waga_w_kg = input("Podaj wage w KG: ")
print("Waga to:",waga_w_kg,"w KG")

wzrost_w_metrach = input("podaj wzrost w metrach: ")
print("Wzrpst to:",wzrost_w_metrach,"w metrach")


waga_w_kg = float(waga_w_kg.replace(",","."))
wzrost_w_metrach = float(wzrost_w_metrach.replace(",","."))

bmi = waga_w_kg/(wzrost_w_metrach**2)
print("Twoje BMI to:",round(bmi,2))
