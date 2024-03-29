"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

A file of checkers.
"""

def CheckFloatNum(num : str) -> bool:
    '''
    CheckFloatNum(str) - Checks whether the input value is a real number.
        Args:
            num (str): Input value.
        Returns:
            bool: True if the input value is a real number, otherwise False.
    '''
    try:
        num = float(num)
        return True
    except:
        return False
    
def CheckIntNum(num : str) -> bool:
    '''
    Checks whether the input value is an integer.
        Args:
            num (str): Input value.
        Returns:
            bool: True if the input value is an integer, otherwise False.
    '''
    try:
        num = int(num)
        return True
    except:
        return False