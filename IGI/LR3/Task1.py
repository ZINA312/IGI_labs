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
    print('----Вычислить ln(x+1), вывести x, n, F(x), Math F(x), eps----')
    x = XInputTask1()
    eps = EPSInputTask1()
    res = NaturalLog(x, eps)
    print(f"x = {res['x']}\nn = {res['n']}\nF(x) = {res['F(x)']}\nMath F(x) = {res['Math F(x)']}\neps = {res['eps']}")

def NaturalLog(x: float, eps: float) -> dict:
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