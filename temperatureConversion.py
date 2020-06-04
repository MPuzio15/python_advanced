print("This program can calculate the temperature in Celsius and Fahrenheit degrees.")

def CtempConverter(f):
    result = (f-32)/1.8
    print("The temperature in Celsius is ", result, " degrees")

def fTempConverter(c):
    result = 1.8* c + 32
    print("The temperature in Fahrenheit is " , result, "degrees")

conversionType = input("Choose conversion: \nC - Celsius \nF - Fahrenheit \n")

if(conversionType.lower() == "c"):
        f = int(input("Provide the temperature in Fahrenheit degrees: \n"))
        CtempConverter(f)
elif(conversionType.lower() == "f"):
    c = int(input("Provide the temperature in Celsius degrees: \n"))
    fTempConverter(c)

print()
