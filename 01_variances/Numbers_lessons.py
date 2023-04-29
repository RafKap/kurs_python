# DO DOMU ZROBIC INPUT ITD
spalannie_na_100km = float(input("Podaj spalanie : "))
dystans_w_km = float(input("Podaj dystans w km : "))
litr_benzyny = float(input("Podaj cene za litr benzyny : "))

# spalannie_na_100km = float(spalannie_na_100km.replace(",","."))
# dystans_w_km = float(dystans_w_km.replace(",","."))
# litr_benzyny = float(litr_benzyny.replace(",","."))

koszt = dystans_w_km * (spalannie_na_100km / 100) * litr_benzyny
koszt = round(koszt, 2)
print(koszt)
