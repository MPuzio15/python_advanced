roman_numerals = dict({1:"I", 5:"V", 4:"IV", 9:"IX", 10:"X", 40:"XL", 50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
)
list1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]

x = int(input("Insert a number: "))
key_list = list(roman_numerals.keys())
val_list = list(roman_numerals.values())

def convert_to_roman(x):
    y = val_list[key_list.index(x)]
    return y

print(convert_to_roman(x))


