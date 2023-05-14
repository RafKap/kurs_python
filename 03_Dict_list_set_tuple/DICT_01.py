"""1▹ Utwórz listę lists_to_dict
zawierającą listy 2 elementowe.
Przekształć ją w słownik
dict_from_list."""


lists_to_dict = [
    [1, "A"],
    [2, "B"]
]

dict_from_list = dict(lists_to_dict)
print(dict_from_list)

for k, v in dict_from_list.items():
    print(k, "->", v)
