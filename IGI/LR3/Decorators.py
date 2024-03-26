"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

The decorator checks whether an int or other array has been passed.
"""


def CheckIntList(func):
    def wrapper(arr):
        if isinstance(arr, list) and all(isinstance(element, int) for element in arr):
            return func(arr)
        else:
            raise ValueError("The argument must be a list of integers.")
    return wrapper