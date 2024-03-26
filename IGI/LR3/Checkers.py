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
    try:
        num = float(num)
        return True
    except:
        return False
    
def CheckIntNum(num : str) -> bool:
    try:
        num = int(num)
        return True
    except:
        return False