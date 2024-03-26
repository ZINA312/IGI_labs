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
    count = 0
    for item in lst:
        count += CheckNaturalNum(item)
    return count

def CheckNaturalNum(num : int) -> int:
    if num > 0:
        return 1
    return 0