import math
print("This program calculates the area of a triangle using two sides and the angle between them (in degrees).")
a = float(input("Enter the length of the first side (a): "))
b = float(input("Enter the length of the second side (b): "))
c = float(input("Enter the angle between the two sides (in degrees): "))
angle = math.radians(c)
area = 1/2 * a*b*math.sin(angle)
print("area = ",area)