speed = int(input("Inserta speed in km/h \n" ))

def convert_to_m_per_s(speed):
    speed_in_m_s = (speed * 1000)/3600
    return speed_in_m_s

print("In m/s: ", convert_to_m_per_s(speed))

def convert_to_miles(speed):
    miles_per_hour = 0.6214 * speed
    return miles_per_hour
print("Miles per hour: ", convert_to_miles(speed))
