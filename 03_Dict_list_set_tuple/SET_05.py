"""
Porównaj zachowanie discard() vs remove() dla typu set.
"""

set_test = {1, 2, 3, 4}


set_test.discard(5)
print(set_test)


## remove wywala blad jezeli dana wartosc nie istnieje w SET
set_test = {1, 2, 3, 4}
set_test.remove(35)
print(set_test)