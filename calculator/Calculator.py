from math import log
import mpmath
import sympy

class Calculator:

    def add(self,a, b):

        return a + b

    def division(self,a,b):

        return a/b

    def logarithm(self,basis,value):

        return log(basis, value)

    def derivative(self,equation, variable):
        return sympy.diff(equation, variable)

