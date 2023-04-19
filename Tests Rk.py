print("\n\tHello World!")
print ()

# List check
lst1 = [1,3,5,6,7,8]
lst2 = [1,2,3,4,5,6,7]

lista3 = list(set(lst1)&set(lst2))

print(lista3)
print()


## String index - powinno rozlozyc RAFAL na kolejne linie w print


text_to_index = "Rafal"
len(text_to_index)
#print(len(text_to_index))
b = len(text_to_index)
print(b)
print()


number = 0
a = text_to_index[number]
print(a)
number = number + 1
a = text_to_index[number]
print(a,"\n")

number = 0
#number = int(number)

while number < 5:
    a = text_to_index[number]
    print(a,)
    number = number +1