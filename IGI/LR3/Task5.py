"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

Queries the list and finds the sum of the odd elements and the sum of the elements between the first and last negative numbers.
"""

from InputFuncs import LengthInputTask5, ListInputTask5
from Generators import GenerateFloatList

def RunTask5():
    '''
    Starts Task 5: List processing.
    Prompts the user to choose to enter a list (manually or generate a list) and performs two subtasks:
        - Find the sum of the list items with odd numbers.
        - Find the sum of the list items located between the first and last negative elements.
        Args:
            None
        Returns:
            None
    '''
    print('----Найти сумму элементов списка с нечетными номерами и сумму элементов списка, расположенных между первым и последним отрицательными элементами----')
    while True:
        menu = input("1. Ввод вручную\n2. Сгенерировать список\nВвод: ")
        match menu:
            case '1':
                listLength = LengthInputTask5()
                mainList = ListInputTask5(listLength)
                break
            case '2':
                listLength = LengthInputTask5()
                mainList = list(GenerateFloatList(-10, 10, listLength))
                break
            case _:
                print('Нет такого варианта!')
                continue
    print(f'Список: {", ".join(map(str, mainList))}')
    print(f'Сумма нечетных элементов: {SumOfOddElements(mainList)}')
    print(f'Сумма элементов между первым и последним отрицательными элементами: {SumOfElemsBetweenNegatives(mainList)}')

def SumOfOddElements(lst : list) -> float:
    '''
    Calculates the sum of the list items with odd numbers.
        Args:
            lst (list): The input list.
        Returns:
            float: The sum of the elements with odd numbers.
    '''
    oddSum = 0
    for i in range(len(lst)):
        if i % 2 != 0:  # Проверяем нечетность индекса
            oddSum += lst[i]
    return oddSum

def SumOfElemsBetweenNegatives(lst : list) -> float:
    '''
    Calculates the sum of the list items located between the first and last negative elements.
        Args:
            lst (list): The input list.
        Returns:
            float: The sum of the elements between the first and last negative elements.
    '''
    firstNegIndex = -1
    lastNegIndex = -1
    for i in range(len(lst)):
        if lst[i] < 0:
            if firstNegIndex == -1:
                firstNegIndex = i
            lastNegIndex = i
    if firstNegIndex == -1 or lastNegIndex == -1:
        return 0 
    else:
        elemsSum = sum(lst[firstNegIndex+1:lastNegIndex])
        return elemsSum