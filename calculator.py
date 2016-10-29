running = True

print("Hello! I'm a simple, smart calculator and would love to do some maths for you :)")
print("Let's start!")

operators = ["+", "-", "*", "/"]    #we are doing a list of operators we can use

while running:

    try:
        operand1 = int(input('Enter first number (or letter if you are already '
                             'giving up and wish to exit):'))    #if it won't be a number program will exit
    except ValueError:
        print("Goodby and see you next time!")
        exit()
    op = input("Enter an operator (+,-,* or /):")
    if op in operators:   #we are checking if the operator we use is on the list of operators
        try:
            operand2 = int(input("Enter second number:"))    #we can't put anything else than number
        except ValueError:
            print("Oups! That's not a number...")
            print("Don't give up, try again!")
            continue
        if op == "+":    #calculator is checking which operator was used
            result = operand1 + operand2
            print(operand1, "+", operand2, "=", result)
            print("I'm ready to do some more math!")
        elif op == "-":
            result = operand1 - operand2
            print(operand1, "-", operand2, "=", result)
            print("I'm ready to do some more math!")
        elif op == "*":
            result = operand1 * operand2
            print(operand1, "*", operand2, "=", result)
            print("I'm ready to do some more math!")
        elif op == "/":
            result = operand1 / operand2
            print(operand1, "/", operand2, "=", result)
            print("I'm ready to do some more math!")
    else:
        print("It wasn't operator i expect...")    #if we make a mistake the calculator will give us another chance
        print("Don't give up, try again!")
