"""
Program: Tasks Execution
Lab Work: 4th Lab Work
Title: Working with Files, Classes, Serializers, Regular Expressions, and Standard Libraries
Version: 1
Developer: Kudosh Alexey
Date: 06.05.2024
"""

import os
from Task1.Task1 import Task1
from Task2.Task2 import Task2
from Task3.Task3 import Task3
from Task4.Task4 import Task4
from Task5.Task5 import Task5

def show_menu():
    """
    Displays the menu of tasks.
    """
    print("===== Tasks menu =====")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("4. Task 4")
    print("5. Task 5")
    print("0. Exit")
    print("------------------------")

def main():
    """
    Main function that runs the program and handles user input.
    """
    while True:
        show_menu()
        choice = input("Enter the task number (from 1 to 5) or 0 to exit: ")

        if choice == "1":
            os.system('cls')
            Task1()  # Executes Task1 function
        elif choice == "2":
            os.system('cls')
            Task2()  # Executes Task2 function
        elif choice == "3":
            os.system('cls')
            Task3()  # Executes Task3 function
        elif choice == "4":
            os.system('cls')
            Task4()  # Executes Task4 function
        elif choice == "5":
            os.system('cls')
            Task5()  # Executes Task5 function
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Wrong input, try again!")

if __name__ == '__main__':
    main()