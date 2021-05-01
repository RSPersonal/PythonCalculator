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
            return print(value_error)

    @classmethod
    def is_numeric(cls, input_text):
        """A method to check if input text is an integer or float"""
        try:
            if int(input_text) or isinstance(input_text, int) or input_text.isdigit():
                return True
        except TypeError as type_error:
            return print(type_error)

    @classmethod
    def convert_to_int_or_float(cls, input_string):
        """A method to convert the input to int or float"""
        if input_string.isdigit():
            converted_integer = int(input_string)
            return converted_integer
        elif float(input_string):
            return float(input_string)
        else:
            return print("Input was not convertable to integer")

operations =  {
    "+" : Calculator.add,
    "-" : Calculator.substract,
    "*" : Calculator.multiply,
    "/" : Calculator.divide
}
