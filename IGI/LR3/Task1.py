"""
Lab Work 3: Python
Version: 1.0
Developer: Alexey Kudosh
Group: 253503
Option: 13
Date: 22.03.2024

Calculates the natural logarithm through the sum and the built-in function.
"""

import math
from InputFuncs import XInputTask1, EPSInputTask1

def RunTask1() -> None:
    '''
    Performs Task 1: Calculate ln(x+1) and output the results. Asks the user for the value of 'x' and the desired precision of 'eps' to calculate the natural logarithm (x+1). It then calls the NaturalLog function to perform calculations and outputs the results.
        Args:
            None
        Returns:
            None
    '''
    print('----Вычислить ln(x+1), вывести x, n, F(x), Math F(x), eps----')
    x = XInputTask1()
    eps = EPSInputTask1()
    res = NaturalLog(x, eps)
    print(f"x = {res['x']}\nn = {res['n']}\nF(x) = {res['F(x)']}\nMath F(x) = {res['Math F(x)']}\neps = {res['eps']}")

def NaturalLog(x: float, eps: float) -> dict:
    '''
    Calculates the natural logarithm (x+1) with a given precision of 'eps'. It uses the Taylor series to approximate the value of the logarithm.
        Args:
            x (float): The value of 'x' to calculate the natural logarithm for.
            eps (float): The required accuracy for calculation.
        Returns:
            dict: A dictionary with the results of calculations, including the following keys:
                - 'x': The value of 'x' passed to the function.
                - 'n': The number of iterations performed to achieve the specified accuracy.
                - 'F(x)': Approximate value of the natural logarithm (x+1).
                - 'Math F(x)': The exact value of the natural logarithm (x+1) calculated using the math.log(1 + x) function.
                - 'eps': The specified accuracy of 'eps'.
    '''
    result = {}
    result['x'] = x
    result['Math F(x)'] = math.log(1 + x)
    result['eps'] = eps
 
    t = eps + 1
    n = 1
    sumres = 0.

    while abs(t) > eps:
        t = sumres
        sumres += math.pow(-1, n - 1)*(math.pow(x, n)/n)
        n += 1
        t = sumres - t
    
    result['F(x)'] = sumres
    result['n'] = n - 1

    return result