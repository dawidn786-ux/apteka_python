'''
NAME
    advancedfun

DESCRIPTION
    This module allows the user to print the result of a simple equation,
    such as x+y, x-y, and others for various values of input parameters (x or x, y)

    This tool accepts file (.txt) that includes equation as text.

    This script requires ..... (name of package) be installed within the Python
    environment you are running this script in.

FUNCTIONS
    This module contains the following functions:
    * calculated_equation(f(x,y),x,y) - returns the value of f(x,y) for x,y where
    f(x) is equation eg. 2*x

    * calculated_fun(f(x,y),x,y) - returns the value of A*(x+y) for f(x,y) = addition
    or B*(x-y) for f(x,y) = subtraction; globals.py contains A,B.

    * calculated_equation_with_file(f(x),x) - returns the value of f(x) for x where
     f(x) is equation in equation.txt file

EXAMPLES
    calculated_fun(addition, x=2, y=3)
    calculated_equation(equation='2*x', x=5)
    calculated_equation_with_file(file='equation.txt', x=5)
'''

import os
from additionfun0 import *

def calculated_fun(fun, x, y):  # fun is outer function (AdditionFun0)
    result = fun(x, y)
    print('Result calculated_fun(): ', result)

def calculated_equation(equation, x):
    print('Result calculated_equation(): ', eval(equation))

def calculated_equation_with_file(file, x):
    with open(file) as my_file:
        print('Result calculated_equation(): ', eval(my_file.read()))

