def sum_natural_for(n):
    sum_nr = 0
    for i in range(1, n+1, 1):
        sum_nr += i
        print(i, "suma akutalna:", sum_nr)

    return sum_nr


print(sum_natural_for(10))