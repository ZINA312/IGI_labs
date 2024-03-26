"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

Requests a string and determines whether it is an octal number.
"""


from InputFuncs import StringInputTask3

def RunTask3():
    print('----Определить, является ли введенная с клавиатуры строка восьмеричным числом----')
    string = StringInputTask3()
    if IsOctalNum(string):
        print('Число является восьмеричным')
    else:
        print('Число не является восьмеричным')

def IsOctalNum(string : str) -> bool:
    try:
        value = int(string, 8)
        if oct(value)[2:] == string:
            return True
    except: pass
    return False