import math
import random

# Task 1, greeting

Name = input("What is your name?")
print("Welcome", Name)

# Task 2, area of the circle

radius = int(input("Enter the radius: "))
pi = math.pi
Area_of_the_Circle = pi*radius
print(f"Area of the circle is: {round(Area_of_the_Circle, 2)}")


# Task 3, Area and perimeter of rectangle

length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print(f"Area is: {area} ")
print(f"Perimeter is: {perimeter}")

# Task 4, Sum, product, and average of numbers

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third  number: "))

sum_of_numbers = first_number + second_number + third_number
product_of_numbers = first_number * second_number * third_number
average_of_numbers = round((first_number + second_number + third_number) / 3, 2)
print(f"sum of the numbers is {sum_of_numbers}")
print(f"product of the numbers is {product_of_numbers}")
print(f"average of the numbers is {average_of_numbers}")

# task 5, mass in medieval units

mass_in_talents = float(input("Enter mass in talents: "))
mass_in_pounds = float(input("Enter mass in pounds: "))
mass_in_lots = float(input("Enter mass in lots "))

talents_in_kilograms = mass_in_talents * 20 * 32 * 13.3 * 0.001
pounds_in_kilograms = mass_in_pounds * 32 * 13.3 * 0.001
lots_in_kilograms = mass_in_lots * 13.3 * 0.001

Weight = round(talents_in_kilograms + pounds_in_kilograms + lots_in_kilograms ,5)
grams = round(Weight % 1, 5) * 1000

print("The weight in modern units: ")
print(math.trunc(Weight), "kgs and",math.trunc(grams),"grams")



# Task 6, combinations of numbers for a combination lock


three_digit_code = random.randint(100, 999)

print(f"3 digit code: {three_digit_code}")


digit_1 = str(random.randint(1, 6))
digit_2 = str(random.randint(1, 6))
digit_3 = str(random.randint(1, 6))
digit_4 = str(random.randint(1, 6))

four_digit_code = digit_1 + digit_2 + digit_3 + digit_4

print(f"4 digit code: {four_digit_code}")
