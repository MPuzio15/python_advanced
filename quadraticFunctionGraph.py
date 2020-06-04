import matplotlib.pyplot as plt

'''Prepare the graph of the following quadratic function: f(x) = a*x^2 + b*x + c,
where x = <-10;10> step 1,
and: a = 1, b = -3, c = 1.'''

a=1
b=-3
c=1
y=[]
x=[]

def quadraticFunction(x):
    return(a*x**2+b*x+c)

for i in range(-10,10,1):
    y.append(quadraticFunction(i))
    x.append(i)

print(x)
print(y)
plt.plot(x, y, "o:", color="green", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykres")
plt.show()