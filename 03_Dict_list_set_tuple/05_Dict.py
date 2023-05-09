"""
W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
"""

poem = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

poem = poem.lower().replace(",", "").split()

counting_word = {}

for word in poem:
    if word in counting_word:
        counting_word[word] = counting_word[word] + 1
    else:
        counting_word[word] = 1

for k, v in counting_word.items():
    print("*", k, "wystepuje:", v)
