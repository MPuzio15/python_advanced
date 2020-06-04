import matplotlib.pyplot as plt
osx=[]
osy=[]

def rownanieCollatza(n):
    x = 0
    while n > 1:
        x+=1
        osx.append(x)
        if (n % 2 == 0):
            n = n // 2
        else:
            n = 3 * n + 1
        osy.append(n)

    print("Os X: ", osx,"\nOs Y: ", osy)

n = int(input('Podaj dowolna liczbe calkowita dodatnia: \n'))
rownanieCollatza(n)

plt.plot(osx, osy, "o:", color="darkblue", linewidth=1)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Rownanie Collatza")
plt.show()
