"""The class for all operations"""

import numpy as np

class Calculator:
    """A class for the math operations"""

    @classmethod
    def __init__(cls, n_one, n_two):
        cls.n_one = n_one
        cls.n_two = n_two

    @classmethod
    def add(cls, n_one, n_two):
        """Method for adding"""
        return np.add(n_one, n_two)

    @classmethod
    def substract(cls,  n_one, n_two):
        """Method for substracting"""
        return  np.subtract(n_one, n_two)

    @classmethod
    def multiply(cls,  n_one, n_two):
        """Method for multiplying"""
        return  np.multiply(n_one, n_two)

    @classmethod
    def divide(cls,  n_one, n_two):
        """Method for dividing"""
        return  n_one / n_two

    @classmethod
    def result(cls, symbol, num_one, num_two):
        """Method for calculating the result"""
        try:
            calculation_function = operations[symbol]
            answer = calculation_function(num_one, num_two)
            return answer
        except ValueError as value_error:
            print(value_error)

operations =  {
    "+" : Calculator.add,
    "-" : Calculator.substract,
    "*" : Calculator.multiply,
    "/" : Calculator.divide
}
