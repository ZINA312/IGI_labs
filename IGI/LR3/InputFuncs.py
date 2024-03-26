"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

A file of input functions.
"""

from Generators import GenerateIntList, GenerateFloatList
from Checkers import CheckIntNum, CheckFloatNum
from Data import task4DefaultString

def XInputTask1() -> float:
    while True:
        x = input('Введите x: ')
        if not CheckFloatNum(x):
            print('x должен быть числом!')
            continue
        break
    return float(x)

def EPSInputTask1() -> float:
    while True:
        eps = input('Введите eps: ')
        if not CheckFloatNum(eps):
            print('eps должен быть числом!')
            continue
        break
    return float(eps)

def ManualInputTask2() -> list:      
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
    return list(GenerateIntList(-10, 10, 20))

def StringInputTask3() -> str:
    return(input('Введите строку: '))

def ManualInputTask4() -> str:     
    return(input('Введите строку: '))

def DefaultInputTask4() -> str:
    return(task4DefaultString)
    
def LengthInputTask5() -> int:
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