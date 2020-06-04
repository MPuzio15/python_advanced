'''
def max(a, b ,c ):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
'''
def maxValue(a,b,c):
    return max(a,b,c)

'''
def min(a, b ,c ):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c
'''
def minValue(a,b,c):
    return min(a,b,c)

print("Provide 3 different numbers, program will return max or min value")
a = int(input("First number: \n"))
b = int(input("Second number: \n"))
c = int(input("Third number: \n"))


def returnMaxOrMin():
    maxOrMin = input("Choose which value should be returned: max / min \t")
    if (maxOrMin == "max"):
        print("Max value is: " , maxValue(a,b,c))
    elif (maxOrMin == "min"):
        print("Min value is: " , minValue(a,b,c))

returnMaxOrMin()



