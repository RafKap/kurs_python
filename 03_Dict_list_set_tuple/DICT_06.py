" 6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów"

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}

lista_1 =[]

for values in days.values():
    lista_1.append(values)

lista_1 = list(dict.fromkeys(lista_1))
print(lista_1)

