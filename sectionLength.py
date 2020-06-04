import math

print("Provide the value of x1,x2,y1 and y2: ")
x1 = int(input("X1 = \t"))
x2 = int(input("X2 = \t"))
y1 = int(input("Y1 = \t"))
y2 = int(input("Y2 = \t"))

def sectionLength(x1,x2, y1, y2):
    length = abs(math.sqrt((x2 -x1) ** 2 + (y2 - y1)**2))
    print("Section length = ", length)

sectionLength(x1,x2, y1, y2)