
from abc import ABC, abstractmethod

class AbstractCalculator (ABC):
    @abstractmethod
    def add(self, a, b):
        pass
        #adition of two values

    @abstractmethod
    def diversion(self, a, b):
        pass
        #division of two values

    @abstractmethod
    def logarithm(self, basis, value):
        pass
        #logarithm of base from value

    @abstractmethod
    def derivative(self,equation, variable ):
        pass
        #derivative of variable
