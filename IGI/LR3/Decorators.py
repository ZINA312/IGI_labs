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
    '''
    The CheckIntList decorator(func) contains:
        wrapper(arr) - Checks whether the function argument is a list of integers.
        Args:
            arr (list): A list of items.
        Returns:
            The result of executing the original function.
        Raises:
            ValueError: If the argument is not a list of integers.
    '''
    def wrapper(arr):
        if isinstance(arr, list) and all(isinstance(element, int) for element in arr):
            return func(arr)
        else:
            raise ValueError("The argument must be a list of integers.")
    return wrapper