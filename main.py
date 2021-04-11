#! Python 3.9  - A python calculator

#Dependencies
from operations import Calculator, operations
from visuals import logo


#Declaring variable for user 
exit = False

while not exit:
    print(logo)
    num1 = int(input("Whats the first number? "))
    num2 = int(input("Whats the second number? "))

    #Showing all the operation options to the user
    for operation in operations:
        print(operation)

    #Getting the symbol from user input 
    operation_symbol = input("Pick an operation from the line above: ")
    
    #Declaring empty variable for later use
    answer = 0
    
    #Calling the Calculator class with the result method for the result 
    answer = Calculator().result(operation_symbol, num1, num2)

    #Printing the ASCII art to console and the result string
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    #Checking if user wants to continue or not
    continue_calculation = input("Would you like to do further calculations with the answer?")

    #Declaring variable to check if user wants to continue or not
    further_calculations = False

    #
    while not further_calculations:
            
        if continue_calculation == 'Y' or continue_calculation == 'y':

            old_answer = answer

            for operation in operations:
                print(operation)

            operation_symbol = input("Pick an operation from the line above: ")

            num3 = int(input("Please enter your number: "))

            answer = Calculator().result(operation_symbol, answer, num3)
            print(f"{old_answer} {operation_symbol} {num3} = {answer}")

            continue_calculation = input("Would you like to do further calculations with the answer?")

            print()
            if continue_calculation == 'Y' or continue_calculation == 'y':
                old_answer = answer
                continue
            else:
                further_calculations = True
                break
    else:
        exit = True 
        break
        