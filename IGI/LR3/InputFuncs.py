"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

A file of input functions.
"""

from Generators import GenerateIntList
from Checkers import CheckIntNum, CheckFloatNum
from Data import task4DefaultString

def XInputTask1() -> float:
    '''
    A function for entering the value of x for task 1.
    Requests the value of x, checks it, and returns it for task 1.
        Args:
            None
        Returns:
            float: The entered value of x.
    '''
    while True:
        x = input('Введите x: ')
        if not CheckFloatNum(x):
            print('x должен быть числом!')
            continue
        break
    return float(x)

def EPSInputTask1() -> float:
    '''
    A function for entering the value of x for task 1.
    Requests the value of x, checks it, and returns it for task 1.
        Args:
            None
        Returns:
            float: The entered value of x.
    '''
    while True:
        eps = input('Введите eps: ')
        if not CheckFloatNum(eps):
            print('eps должен быть числом!')
            continue
        break
    return float(eps)

def ManualInputTask2() -> list:  
    '''
    A function for manually entering a list of integers for task 2.
    Requests integers and checks them. When you enter 0, it completes the loop and returns a list of numbers.
        Args:
            None
        Returns:
            list: A list of integers.
    '''    
    numList = list()    
    while True:
        num = input('Введите целое число(для завершения 0): ')
        if not CheckIntNum(num):
            print('Это не целое число!')
            continue
        num = int(num)
        if num == 0:
            break
        numList.append(int(num))
    return numList

def GenerativeInputTask2() -> list:
    '''
    A function for generating a random list of integers for task 2.
    Uses the generator from the module "Generators.py ".
        Args:
            None
        Returns:
            list: A list of integers.
    '''
    return list(GenerateIntList(-10, 10, LengthInputTask5()))

def StringInputTask3() -> str:
    '''
    A function for entering a string for task 3.
    Requests a string to be entered.
        Args:
            None
        Returns:
            str: The entered string.
    '''
    return(input('Введите строку: '))

def ManualInputTask4() -> str: 
    '''
    A function for entering a line for task 4.
    Requests a string to be entered.
        Args:
            None
        Returns:
            str: The entered string.
    '''    
    return(input('Введите строку: '))

def DefaultInputTask4() -> str:
    '''
    A function to get the default string value for task 4.
    Returns the default string from the module "Data.py "
        Args:   
            None
        Returns:
            str: The default string value.
    '''
    return(task4DefaultString)
    
def LengthInputTask5() -> int:
    '''
    A function for entering the number of list items for task 5.
    Requests an integer and checks it.
        Args:   
            None
        Returns:
            int: The entered number of list items
    '''
    while True:
        length = input('Введите количество элементов списка: ')
        if not CheckIntNum(length):
            print('Количество должно быть целым числом!')
            continue
        length = int(length)
        if (length <= 0):
            print('Количество должно быть больше 0!')
            continue
        break
    return length

def ListInputTask5(length : int) -> list:
    '''
    A function for manually entering list items for task 5.
    Requests real elements and verifies them.
        Args:
            length (int): The number of items in the list.
        Returns:
            list: A list of real numbers.
    '''
    resList = list()
    for i in range(0, length):
        while True:
            item = input(f'Введите {i + 1} элемент списка: ')
            if not CheckFloatNum(item):
                print('Элемент должен быть вещественным числом!')
                continue
            break
        resList.append(float(item))
    return resList