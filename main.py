#! Python 3.9  - A python calculator

#Dependencies
from operations import Calculator, operations
from visuals import logo


#Declaring variable for user 
exit = False

while not exit:
    print(logo)

    #Declaring varible of check 
    numeric_num1 = False

    #While loop to check if the input is numeric 
    while not numeric_num1:
        #Getting the input for number 1 from the user
        num1 = input("Whats the first number? ")
        num1 = Calculator().convert_to_int(num1)

        if Calculator().is_numeric(num1): 
            numeric_num1 = True
            break
        else:
            print("Please enter a integer or float!")
            num1 = int(input("Whats the first number? "))

            if Calculator().is_numeric(num1):
                break

            continue
    
    #Declaring variable for check
    numeric_num2 = False
    
    while not numeric_num2:
        num2 = int(input("Whats the second number? "))
        if Calculator().is_numeric(num2):
            numeric_num2 = True
            break
        else:
            continue

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

            if continue_calculation == 'Y' or continue_calculation == 'y':
                old_answer = answer
                continue
            else:
                further_calculations = True
                break
    else:
        exit = True 
        break
        