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
    for i in range(0,count):
        yield random.randint(fromNum, toNum + 1)

def GenerateFloatList(fromNum: float, toNum : float, count :int):
    for i in range(0,count):
        yield random.uniform(fromNum, toNum)