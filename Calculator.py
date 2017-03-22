from math import log
import mpmath
import sympy
from Validator import Validator
from Exceptions import  Not_A_String, Not_A_Number, Not_A_Possible_Denominator, Not_A_Possible_Basis, Not_A_Positive_Value
class Calculator:

    def add(self,a, b):
        if not Validator._number_or_not(a):
            raise Not_A_Number(a)
        if not Validator._number_or_not(b):
            raise Not_A_Number(b)
        return a + b

    def division(self,a,b):
        if not Validator._number_or_not(a):
            raise Not_A_Number(a)
        if not Validator._number_or_not(b):
            raise Not_A_Number(b)
        if not Validator._possible_denominator_or_not(b):
            raise Not_A_Possible_Denominator(b)
        return a/b

    def logarithm(self,basis,value):
        if not Validator._number_or_not(basis):
            raise Not_A_Number(basis)
        if not Validator._number_or_not(value):
            raise Not_A_Number(value)
        if not Validator._possible_basis_or_not(basis):
            raise Not_A_Possible_Basis(basis)
        if not Validator._possible_value_or_not(value):
            raise Not_A_Positive_Value(value)
        return log( value,basis)

    def derivative(self,equation, variable):
        return sympy.diff(equation, variable)



