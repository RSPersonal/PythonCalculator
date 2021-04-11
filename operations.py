
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
            print(e)

operations =  {
    "+" : Calculator.add,
    "-" : Calculator.substract,
    "*" : Calculator.multiply,
    "/" : Calculator.divide
    }