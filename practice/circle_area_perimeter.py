"""
This code calculates the area and circumference of a circle
based on the radius provided by the user.
"""

pi = 3.14

radius = float(input('Radius: '))

area = (pi * radius **2)
circumference = (2 * pi * radius)

print(area)
print(circumference)
