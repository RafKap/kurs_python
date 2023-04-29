"""Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy,
utwórz nowy łańcuch s3, dołączając s2 w środku s1."""

s1 = "abcd"
s2 = "1234"

s3 = s1[:2:] + s2 + s1[2::]
print(s3)
