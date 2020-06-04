income = float(input("Insert your brutto input: "))

def tax(income):
    if income<= 1000:
        tax = 0
        print("Your tax is 0")
    elif (income > 1000 and income <= 85000):
        tax = income*0.17
        print("Your tax: ", tax)
    elif(income>85000):
        tax = income * 0.32
        print("Your tax: ", tax)
    else:
        print("Incorrect format")

tax(income)