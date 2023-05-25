def max_of_two(val1, val2):
    return val1 if val1 > val2 else val2


def max_of_tree(a, b, c):
    return max_of_two(c, max_of_two(a, b))
