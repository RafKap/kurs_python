"""
Nie korzystając z funkcji wbudowanej min(),
napisz funkcję znajdującą minimalną wartość z 3 liczb.
minimum_of(a, b, c).
"""

def min_of_two(val1, val2):
    return val2 if val1 > val2 else val1


def min_of_tree(a, b, c):
    return min_of_two(c, min_of_two(a, b))


def main():
    x, y, z = [11, 13, 2]
    print(min_of_tree(x, y, z))


main()