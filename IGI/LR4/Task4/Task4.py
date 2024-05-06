"""
Program: Task 4
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

import re
import os
from .GeometricShape import GeometricShape
from .ShapeColor import ShapeColor
from .Triangle import Triangle
from Checkers import CheckFloatNum

def validate_color(color):
    """
    Validates the format of a color string.
    Returns True if the color is in the correct format (hexadecimal value), False otherwise.
    """
    pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    if re.match(pattern, color):
        return True
    else:
        return False

def show_menu():
    """
    Displays the menu options for the program.
    """
    print("===== Text Analyzer Program =====")
    print("1. Draw figure")
    print("2. Figure to file")
    print("3. Calculate area")
    print("0. Exit")
    print("----------------------------------")

def Task4():
    """
    Main function that handles user input and performs actions based on the chosen menu option.
    """
    while True:
        while True:
            a = input('Input a:')
            if(CheckFloatNum(a)):
                a = float(a)
                break
            print("Wrong input!")
        while True:
            b = input('Input b:')
            if(CheckFloatNum(b)):
                b = float(b)
                break
            print("Wrong input!")
        while True:
            c = input('Input c:')
            if(CheckFloatNum(c)):
                c = float(c)
                break
            print("Wrong input!")
        if a + b > c and a + c > b and b + c > a:
            break
        else:
            print("This triangle doesn't exist!")
    while True:
        color = input('Input color:')
        if(validate_color(color)):
            break
        print("Wrong input!")
    triangle = Triangle(a, b, c, color)
    os.system('cls')
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        os.system('cls')
        if choice == "1":
            triangle.draw()
        elif choice == "2":
            triangle.draw_to_file("triangle.png")
        elif choice == "3":
            print(f"Area of the triangle: {triangle.calculate_area()}")
        elif choice == "0":
            print("Exiting the Task4...")
            break
        else:
            print("Invalid choice! Please try again.")