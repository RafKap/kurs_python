"""
Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same
"""

lcz = input("Lista: ")
lcz = lcz.split()

if lcz[0] == lcz[-1]:
    print("True")
else:
    print('Not true')