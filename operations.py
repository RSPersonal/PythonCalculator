
class Calculator():
    "A class for the math operations" 
    def add(self, n1, n2):
        return n1 + n2

    def substract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        return n1 / n2

    def result(self, symbol, num1, num2):
        try:
            calculation_function = operations[symbol]
            answer = calculation_function(self, num1, num2)
            return answer
        except Exception as e:
            return print(e)

    def is_numeric(self, input_text):
        """A method to check if input text is an integer or float"""
        try:
            if int(input_text) or isinstance(input_text, int) or input_text.isdigit():
                return True
        except TypeError as e:
            return print(e)

    def convert_to_int_or_float(self, input_string):
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