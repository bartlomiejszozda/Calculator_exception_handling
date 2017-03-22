from Calculator import Calculator
import unittest
from Exceptions import  Not_A_String, Not_A_Number, Not_A_Possible_Denominator, Not_A_Possible_Basis, Not_A_Positive_Value


class CalculatorTest(unittest.TestCase):
    def test_add_two_value_return_result(self):
        calc=Calculator()
        a=12
        b=-123.3
        self.assertEqual(-111.3,calc.add(a,b))

    def test_add_string_and_value_return_exception(self):

         calc=Calculator()
         a="string"
         b=234
         self.assertRaises(Not_A_Number,calc.add, a, b)


    def test_add_string_and_string_return_exception(self):
        calc =Calculator()
        a="string1"
        b="string2"
        self.assertRaises(Not_A_Number,calc.add, a, b)



    def test_division_two_value_return_result(self):
        calc = Calculator()
        a =29.4
        b = -14
        self.assertEqual(-2.1, calc.division(a, b))

    def test_division_value_and_string_return_exception(self):
        calc =Calculator()
        a=31
        b="string"
        self.assertRaises(Not_A_Number,calc.division, a, b)

    def test_division_string_and_string_return_exception(self):
        calc = Calculator()
        a = "string1"
        b = "string2"
        self.assertRaises(Not_A_Number, calc.division, a, b)

    def test_division_by_zero_return_exception(self):
        calc = Calculator()
        a = 123
        b = 0
        self.assertRaises(Not_A_Possible_Denominator, calc.division, a, b)




    def test_logarithm_of_two_value_return_result(self):
        calc = Calculator()
        a = 2.0
        b = 16.0
        self.assertEqual(4.0, calc.logarithm(a, b))

    def test_logarithm_of_string_and_value_return_exception(self):
        calc = Calculator()
        a = "string"
        b = 123
        self.assertRaises(Not_A_Number, calc.logarithm, a, b)

    def test_logarithm_of_string_and_string_return_exception(self):
        calc = Calculator()
        a = "string1"
        b = "string2"
        self.assertRaises(Not_A_Number, calc.logarithm, a, b)

    def test_logarithm_of_basis_lower_than_0_return_exception(self):
        calc = Calculator()
        a = -5
        b = 25
        self.assertRaises(Not_A_Possible_Basis, calc.logarithm, a, b)

    def test_logarithm_of_basis_equal_to_1_return_exception(self):
        calc = Calculator()
        a = 1
        b = 25
        self.assertRaises(Not_A_Possible_Basis, calc.logarithm, a, b)

    def test_logarithm_of_value_lower_than_0_return_exception(self):
        calc = Calculator()
        a = 5
        b = -25
        self.assertRaises(Not_A_Positive_Value, calc.logarithm, a, b)
