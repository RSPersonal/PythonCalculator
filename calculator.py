#! Python 3.9  - A python calculator

#Dependencies
from operations import Calculator, operations
from visuals import logo, instance_calculator, instance_calculator_first_use


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

    #

    print(instance_calculator_first_use)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    continue_calculation = input("Would you like to do further calculations with the answer?")

    further_calculations = False

    while not further_calculations:
            
        if continue_calculation == 'Y' or continue_calculation == 'y':

            old_answer = answer

            for operation in operations:
                print(operation)

            operation_symbol = input("Pick an operation from the line above: ")

            num3 = int(input("Please enter your number: "))

            answer = Calculator().result(operation_symbol, answer, num3)

            instance_calculator = (f"""
            _____________________
            |  _________________  |
            | | {old_answer} {operation_symbol} {num3} = {answer}     | |  
            | |_________________| |
            |  ___ ___ ___   ___  | 
            | | 7 | 8 | 9 | | + | | 
            | |___|___|___| |___| | 
            | | 4 | 5 | 6 | | - | | 
            | |___|___|___| |___| |
            | | 1 | 2 | 3 | | x | | 
            | |___|___|___| |___| | 
            | | . | 0 | = | | / | | 
            | |___|___|___| |___| |  
            |_____________________|
            """)

            print(instance_calculator)
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
        