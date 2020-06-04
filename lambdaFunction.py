import math

square_area = lambda a:a**2
circle_area = lambda r: (math.pi*r)**2
add = lambda x, y :x+y


print(square_area(5))
print(circle_area(4))
print(add(2,3))


for x in range(0, 10):
    value = lambda x: x**2
    print(value(x))


for x in range (0,10):
    value = lambda x: x**3
    print(value(x))
