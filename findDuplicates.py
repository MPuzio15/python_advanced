'''
Napisać program, wykorzystując fukncje, który sprawdzi czy dana lista ma duplikaty
i następnie wyświetli na osobnej liscie jaki to są duplikaty
i na którym miejscu (indekscie) oryginalnej listy znajdowały się.
'''
a=[1,2,3,3,4,4,5,6,7,8,9,0]
new = []
duplicates = []
def findDuplicates(tab):
    for i in tab:

        if i in new:
            duplicates.append(i)

findDuplicates(a)
print(a, new, duplicates)

