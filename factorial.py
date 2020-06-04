number = int(input("Give the number for which the factorial should be calculated: \n"))

def factorial(x):
    sum = 1
    for i in range(1, x+1):
        sum *=i
    return sum
print(factorial(number))