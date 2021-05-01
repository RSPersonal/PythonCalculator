"""Python 3.9  - A python calculator"""

#Dependencies
import sys
from operations import Calculator, operations
from visuals import logo

def main():
    """The main calculator function"""

    print(logo)

    #Declaring varible of check
    numeric_num1 = False

    #While loop to check if the input is numeric
    while not numeric_num1:

        #Getting the input for number 1 from the user
        num1 = input("Whats the first number? ")
        num1 = Calculator().convert_to_int_or_float(num1)

        if Calculator().is_numeric(num1):
            numeric_num1 = True
            break
        else:
            print("Please enter a integer or float!")
            num1 = input("Whats the first number? ")

            if Calculator().is_numeric(num1):
                break


    #Declaring variable for check of number 2
    numeric_num2 = False

    while not numeric_num2:
        num2 = int(input("Whats the second number? "))
        if Calculator().is_numeric(num2):
            numeric_num2 = True
            break
        else:
            print("Please enter a integer or float!")
            num2 = input("Whats the second number? ")
            continue


    #Showing all the operation options to the user
    for operation in operations:
        print(operation)

    #Getting the symbol from user input
    operation_symbol = input("Pick an operation from the line above: ")

    #Declaring empty variable for later use
    answer = 0

    #Calling the Calculator class with the result method for the result
    answer = Calculator(n_one=num_one, n_two=num_two).result(operation_symbol, num_one, num_two)

    #Printing the ASCII art to console and the result string
    print(f"{num_one} {operation_symbol} {num_two} = {answer}")

    #Checking if user wants to continue or not
    continue_calculation = input("Would you like to do further calculations with the answer? (Y/y or N/n): ")

    #Declaring variable to check if user wants to continue or not
    further_calculations = False

    #
    while not further_calculations:

        if 'Y' in continue_calculation or 'y' in continue_calculation:

            old_answer = answer

            for operation in operations:
                print(operation)

            operation_symbol = input("Pick an operation from the line above: ")

            num3 = int(input("Please enter your number: "))

            answer = Calculator().result(operation_symbol, answer, num3)
            print(f"{old_answer} {operation_symbol} {num3} = {answer}")

            continue_calculation = input("Would you like to do further calculations with the answer?: ")

            print()
            if 'Y' in continue_calculation or 'y' in continue_calculation:

                old_answer = answer
            else:
                further_calculations = True
                break
        else:
            sys.exit()

if __name__ == '__main__':
    main()
