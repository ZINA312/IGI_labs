import os
from Task1.Task1 import Task1
from Task5.Task5 import Task5
from Task2.Task2 import Task2
from Task3.Task3 import Task3
from Task4.Task4 import Task4


def show_menu():
    print("===== Tasks menu =====")
    print("1. Task 1")
    print("2. Task 2")
    print("3. Task 3")
    print("4. Task 4")
    print("5. Task 5")
    print("0. Exit")
    print("------------------------")

def main():
    while True:
        show_menu()
        choice = input("Enter the task number (from 1 to 5) or 0 to exit: ")

        if choice == "1":
            os.system('cls')
            Task1()
        elif choice == "2":
            os.system('cls')
            Task2()
        elif choice == "3":
            os.system('cls')
            Task3()
        elif choice == "4":
            os.system('cls')
            Task4()
        elif choice == "5":
            os.system('cls')
            Task5()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Wrong input, try again!")


if __name__ == '__main__':
    main()