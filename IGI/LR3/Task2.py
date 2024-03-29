"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

Creates a list and counts the number of natural numbers.
"""

from InputFuncs import ManualInputTask2, GenerativeInputTask2
from Decorators import CheckIntList
def RunTask2() -> None:
    '''
    Starts Task 2: counting the number of natural numbers in the list.
    Organizes a loop that accepts integers from the user or generates a sequence of numbers. Then it counts the number of natural numbers in the list and outputs the results.

        Args:
        None
        Returns:
        None
    '''
    print('----Организовать цикл, который принимает целые числа и вычисляет количество натуральных чисел. Окончание цикла – ввод 0----')
    mainList = list()
    while True:
        menu = input("1. Ввод вручную\n2. Сгенерировать последовательность\nВвод: ")
        match menu:
            case '1':
                mainList = ManualInputTask2()
                break
            case '2':
                mainList = GenerativeInputTask2()
                break
            case _:
                print('Нет такого варианта!')
                continue 
    print(f'Список: {", ".join(map(str, mainList))}')
    print(f'Количество натуральных чисел: {CountNaturalNum(mainList)}')

@CheckIntList
def CountNaturalNum(lst : list) -> int:
    '''
    Counts the number of natural numbers in the list.
    Accepts a list of integers and counts the number of natural numbers in the list. She uses the `CheckIntList` decorator to check that the list contains only integers.

        Args:
            lst (list): A list of integers.
        Returns:
            int: The number of natural numbers in the list.
    '''
    count = 0
    for item in lst:
        count += CheckNaturalNum(item)
    return count

def CheckNaturalNum(num : int) -> int:
    '''
    Checks whether the number is natural.
    Accepts an integer and checks whether it is natural (greater than zero).

        Args:
            num (int): An integer to check.
        Returns:
            int: 1 if the number is natural, otherwise 0.
    '''
    if num > 0:
        return 1
    return 0