for_how_many_numbers = int(input("Insert a number: "))

def table(for_how_many_numbers):
    for i in range(1,for_how_many_numbers+1):
        for j in range(1, for_how_many_numbers+1 ):
            print(i*j, end="\t")
        print()

table(for_how_many_numbers)