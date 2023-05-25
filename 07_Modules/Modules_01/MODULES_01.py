import task_01.bmi as bmi_calc

a = bmi_calc.bmi()

print(a)

if a == "Nadwaga":
    with open('_modules_01_nadwaga.txt', encoding="UTF-8") as fopen:
        content_list = fopen.read()
        print(content_list)
elif a == "Wychudzenie":
    with open('_modules_01_wychudzenie.txt', encoding="UTF-8") as fopen:
        content_list = fopen.read()
        print(content_list)
elif a == "waga prawidlowa":
    with open('_modules_01_waga_prawidlowa.txt', encoding="UTF-8") as fopen:
        content_list = fopen.read()
        print(content_list)
else:
    with open('_modlues_01_niedowaga.txt', encoding="UTF-8") as fopen:
        content_list = fopen.read()
        print(content_list)