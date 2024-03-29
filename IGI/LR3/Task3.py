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
    '''
    Starts Task 3: checking whether the entered string is an octal number.
    Prompts the user to enter a string and checks whether the entered string is an octal number. Then it outputs the corresponding result.
        Args:
            None
        Returns:
            None
    '''
    print('----Определить, является ли введенная с клавиатуры строка восьмеричным числом----')
    string = StringInputTask3()
    if IsOctalNum(string):
        print('Число является восьмеричным')
    else:
        print('Число не является восьмеричным')

def IsOctalNum(string : str) -> bool:
    '''
    Checks whether the string is an octal number.
    Accepts a string and checks if it is an octal number. It tries to convert the string to a base 8 number and then compares the result with the original string. If the result of the conversion of the original string matches the original string, then True is returned, otherwise False is returned.
        Args:
            string (str): The input string to check.
        Returns:
            bool: True if the string is an octal number, otherwise False.
    '''
    try:
        value = int(string, 8)
        if oct(value)[2:] == string:
            return True
    except: pass
    return False