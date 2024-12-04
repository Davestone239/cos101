import math
from random import choice


def area_of_circle():
    radius = float(input('Enter Radius: '))
    area = 2 * 22/7 * radius
    print(area)

#area_of_circle()

def calculate_velocity():
    distance = float(input('Enter Displacement: '))
    time = int(input('Enter Time: '))
    velocity = distance/time
    print(velocity)

#calculate_velocity()


def q():
    velocity = float(input('Enter Velocity: '))
    time = int(input('Enter Time: '))
    speed = velocity/time
    print(speed)

#q()


print("Welcome to Physics 101 class")
print("We have all basic formulas on the topic Projectile Motion And Resultant Of Two Vectors")
print("If you wish to calculate the following properties of a projectile or the resultant of two vectors, use the specified lettering as a reply to the calculation section below")
print("Time of flight = a")
print("Time to reach maximum value on y-axis = b")
print("Range = c")
print("Maximum height reached = d")
print("Resultant of two vectors = e")



def a():
    u = int(input("Enter the initial velocity: "))
    g = float(input("Enter the recommended acceleration due to gravity: "))
    o = float(input("Enter angle of projection: "))
    time_of_flight = ((2 * u) * math.sin(o)/ g)
    print(f"{time_of_flight}sec")



def b():
    x = int(input("Enter the initial velocity: "))
    m = float(input("Enter the recommended acceleration due to gravity: "))
    v = float(input("Enter angle of projection: "))
    time_to_reach_maximum_height = x * math.sin(v)/m
    print(f"{time_to_reach_maximum_height}sec")


def c():
    u = int(input("Enter the initial velocity: "))
    g = float(input("Enter the recommended acceleration due to gravity: "))
    o = float(input("Enter angle of projection: "))
    rg = (u * u ) * math.sin((2 * o ))/g
    print(f"{rg}m")

def d():
    u = int(input("Enter the initial velocity: "))
    g = float(input("Enter the recommended acceleration due to gravity: "))
    o = float(input("Enter angle of projection: "))
    maximum_height_reached = (u * u) * math.sin(( o * o ))/ 2 * g
    print(f"{maximum_height_reached}m")

def e():
    x = int(input("Enter the value of the first vector: "))
    y = int(input("Enter the value of the second vector: "))
    rv = math.sqrt((x * x ) + (y * y )**0.5)
    print(f"{rv}")
def main():
    calculation = input("what physics calculation do you want to work on: ")
    if calculation == "a":
        a()
    if calculation == "b":
        b()
    if calculation == "c":
        c()
    if calculation == "d":
        d()
    if calculation == "e":
        e()






if __name__ == '__main__':
    main()
















