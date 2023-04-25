# zad 1
X = "ACD"
a = X.isnumeric()

print(a)


#zad 2

b = X.center(18, "*")
print(b)

# zad 3
c = X.rstrip("123")
print(c)


# zad 4
d = X.isupper()
print(d)



# zad 5
E = "BANANA"
e = E.count("NA")
print(e)

#zad 6
n = "aAd123"
m = n.isalnum() and n.isupper()
print(m)


txt = input("daj tekst: ")
txt = txt.replace(" ", "").upper()
print("To palindrom", txt == txt[::-1])

