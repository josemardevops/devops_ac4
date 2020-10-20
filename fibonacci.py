def sequencia_fibonacci():
    c = 100
    s = 2
    number_1 = 0
    number_2 = 1
    fibonacci = "0,1,"
    while s < c:
        add_fibo = number_1 + number_2
        if s < c - 1:
            fibonacci = fibonacci + str(add_fibo) + ", "
        else:
            fibonacci = fibonacci + str(add_fibo) + "."
        number_1 = number_2
        number_2 = add_fibo
        s += 1
    return fibonacci

fibonacci = sequencia_fibonacci()

print(fibonacci)