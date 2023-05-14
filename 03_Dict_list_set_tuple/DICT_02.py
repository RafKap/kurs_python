"""
Utwórz listę lub krotkę tuples_to_dict
zawierającą krotki 2 elementowe.
Przekształć ją w słownik tuples_to_dict.
"""

tuples_to_dict = [
    [1, "a"],
    [3, "b"]
]

dict_from_truples = dict(tuples_to_dict)
print(dict_from_truples)

for k, v in dict_from_truples.items():
    print(k, "->", v)