n = int(input("Liczba calkowita: "))

for i in range(1, n+1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FooBar")
    elif i % 3 == 0:
        print("Foo")
    elif i % 5 == 0:
        print("bar")
    else:
        print(i)
