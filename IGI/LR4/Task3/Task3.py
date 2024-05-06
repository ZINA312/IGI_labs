import os
from .NaturalLog import NaturalLog
from Checkers import CheckFloatNum

def show_menu():
    print("===== Text Analizer Program =====")
    print("1. Calculate statistics")
    print("2. Create graph")
    print("0. Exit")
    print("----------------------------------")

def Task3():
    while True:
        x = input('Input x:')
        if(CheckFloatNum(x)):
            break
        print("Wrong input!")
    while True:
        eps = input('Input eps:')
        if(CheckFloatNum(eps)):
            break
        print("Wrong input!")
    log_calc = NaturalLog(float(x), float(eps))
    os.system('cls')
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        os.system('cls')
        if choice == "1":
            log_calc.calculate()
            for key, value in log_calc.get_results().items() :
                print (key, value)
        elif choice == "2":
            log_calc.plot_graphs()
            print("Graph has been created!")
        elif choice == "0":
            print("Exiting the task3...")
            break
        else:
            print("Invalid choice! Please try again.")