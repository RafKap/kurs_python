#zad 1
learing_time = 75
my_time = 2

print("Do nauczenia się nowej umiejętności, potrzebuję ok.", learing_time // my_time, "tygodni")

#zad 2
min_in_h=60
h_in_day=24
day_in_week=7

print("W siedem tyg mamy:", day_in_week * h_in_day * min_in_h * 7, "sekund")

#zad 3
waga_w_kg = input("Podaj wage w KG: ")
print("Waga to:",waga_w_kg,"w KG")

wzrost_w_metrach = input("podaj wzrost w metrach: ")
print("Wzrpst to:",wzrost_w_metrach,"w metrach")


waga_w_kg = float(waga_w_kg.replace(",","."))
wzrost_w_metrach = float(wzrost_w_metrach.replace(",","."))

bmi = waga_w_kg/(wzrost_w_metrach**2)
print("Twoje BMI to:",round(bmi,2))

#koniec zad3