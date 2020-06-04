input = int(input("Insert a number: "))

a = 10

def points(input, a):
    if input > a:
        raise ValueError("You've missed")
    elif input>7 and input < a:
        points = 2
        return points
    elif input >4 and input<=7:
        points = 3
        return points
    elif input<=4 and input>1:
        points = 4
        return points
    elif input == 1:
        points = 5
        return points



print("Bravo you've got: ", points(input, a), "points!!")