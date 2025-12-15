import greeting
import geometry as geo
import calculator
from calculator import multiply
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

greeting.greet("Riya")

calculator.add(num1,num2)
multiply(num1,num2)

geo.calc_area_rect(num1,num2)
geo.calc_rect_peri(num1,num2)