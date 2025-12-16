import math_utils

print("Enter details for rectangle: ")
len = int(input("Enter length: "))
bred = int(input("Enter breadth: "))
math_utils.calc_rect_area(len,bred)

print("Enter details for Square: ")
side = int(input("Enter side of square: "))
math_utils.calc_square_area(side)

print("Enter details for circle: ")
rad = int(input("Enter radius of circle: "))
math_utils.calc_circle_area(rad)


