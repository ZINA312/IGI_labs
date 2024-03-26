"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

The main part of the program provides menus and launches other tasks.
"""

import Task1, Task2, Task3, Task4, Task5
import os

def main():
    while True:
        menu = input('Меню:\n1. Задание 1\n2. Задание 2\n3. Задание 3\n4. Задание 4\n5. Задание 5\n0. Выход\nВвод: ')
        match menu:
            case '1':
                os.system('cls')
                Task1.RunTask1()
            case '2':
                os.system('cls')
                Task2.RunTask2()
            case '3':
                os.system('cls')
                Task3.RunTask3()
            case '4':
                os.system('cls')
                Task4.RunTask4()
            case '5':
                os.system('cls')
                Task5.RunTask5()
            case '0':
                os.system('cls')
                break

if __name__ == '__main__':
    main()