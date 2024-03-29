"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

A file of generators.
"""

import random

def GenerateIntList(fromNum : int, toNum : int, count : int):
    '''
    Generates an integer.
        Args:
            fromNum (int): The initial value of the range (inclusive).
            toNum (int): The final value of the range (inclusive).
            count (int): The number of items in the list.
        Returns:
            int: A random integer.
    '''
    for i in range(0,count):
        yield random.randint(fromNum, toNum + 1)

def GenerateFloatList(fromNum: float, toNum : float, count :int):
    '''
    Generates a real number.
        Args:
            fromNum (float): The initial value of the range (inclusive).
            toNum (float): The final value of the range (inclusive).
            count (int): The number of items in the list.
        Returns:
            float: A random real number.
    '''
    for i in range(0,count):
        yield random.uniform(fromNum, toNum)