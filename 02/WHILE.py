# price = 15
# while (price > 10):
#     print(price, "$ -  too much!")
#     price = price - 2
#
# print(price, "$ price is ok")
# print()
#
#
# a = 0
# while a <= 200:
#     C = 5 / 9 * (a - 32)
#     a = a + 20
#     print(int(C))


names = input("Names: ").replace(", ", " ").replace(",", " ").split(" ")
for i in names:
    print("Hello", i)


text = input("String: ")
lower_letters = 0
upper_letters = 0
digits = 0
other = 0

for i in text:
    if i.islower():
        lower_letters = lower_letters + 1
    elif i.isupper():
        upper_letters = upper_letters + 1
    elif i.isdigit():
        digits = digits +1
    else:
        other = other +1

print(" Lower letters", lower_letters, "\n", "Upper letters", upper_letters, "\n", "Digits", digits, "\n", "Other", other, "\n")



