rows = int(input("Insert the rows number \n"))

def pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(1, rows - i+1):
            print(end=' ')
        for j in range(i, 0, -1):
            print(j, end="")
        for j in range(2, i + 1):
            print(j, end="")
        print()


pyramid(rows)
