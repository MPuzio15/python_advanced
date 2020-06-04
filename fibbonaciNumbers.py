def fibbonaci_numbers(n):

    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

x = fibbonaci_numbers(10)
print(x)