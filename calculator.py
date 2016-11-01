running = True


operators = ["+", "-", "*", "/"]    #we are doing a list of operators we can use

while running:

    try:
        operand1 = int(input("Enter a number (or letter to exit):"))    
                             #if it won't be a number program will exit
    except ValueError:
        exit()
    op = input("Enter an operation:")
    if op in operators:   #we are checking if the operator we use is on the list of operators
        try:
            operand2 = int(input("Enter another number:"))    #we can't put anything else than number
        except ValueError:
            print("Invalid sign")
            continue
        if op == "+":    #calculator is checking which operator was used
            result = operand1 + operand2
            print("Result:", result)
        elif op == "-":
            result = operand1 - operand2
            print("Result:", result)
        elif op == "*":
            result = operand1 * operand2
            print("Result:", result)
        elif op == "/":
            result = operand1 / operand2
            print("Result:", result)
    else:
        print("Invalid sign")    #if we make a mistake the calculator will give us another chance
