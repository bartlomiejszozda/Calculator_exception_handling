from math import isclose

class Validator:
    def _string_or_not(value):
        return isinstance (str,value)
    def _number_or_not(value):
        return isinstance (float,value) or  isinstance(int,value)
    def _possible_basis_or_not(value):
        return value>0 and not isclose(value,1,abs_tol=0.0001) and not isclose(value,0,abs_tol=0.0001)

    def _possible_denominator_or_not(value):
        return not isclose(value, 0, abs_tol=0.0001)
    def _positive_value_or_not(value):
        return value>0