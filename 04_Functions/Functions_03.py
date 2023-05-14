"""Nie korzystając z funkcji wbudowanej max(),
napisz funkcję znajdującą maksymalną wartość z 3 liczb.
maximum_of(a, b, c). """


def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2


def max_of_tree(a, b, c):
    return max_of_two(c, max_of_two(a, b))


def main():
    x, y, z = [13, 13, 12]
    print(max_of_tree(x, y, z))


main()
