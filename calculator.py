def calculator (number1,number2,operator):
    '''
    Returns the result of a math equation.
            Parameter:
                number1 (int) : An interger
                number2 (int) : An interger
                aperator(string) : An string
            Returns:
               interger :  result of the math equation
    '''
    if operator in ("+","-","*","/","//","**"):
        if operator == "+":
            result = number1 + number2
            print(result)
        elif operator == "-":
            result = number1 - number2
            print(result)
        elif operator == "*":
            result = number1 * number2
            print(result)
        elif operator == "/":
            result = number1 / number2
            print(result)
        elif operator == "//":
            result = number1 // number2
            print(result)
        elif operator == "**":
            result = number1 ** number2
            print(result)
        else :
            return

def parse_input():
    '''
    Call function calculator to calculator the math equation.
    Ask userinput for the equation, parse to function calculator.
            Parameters:
                no parameter
            Returns:
                return when one if condition satisified
    '''
    equation = input("Enter equation:")
    if "//" in equation:
        operator = "//"
        n1,n2 = equation.split("//")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return
    if "**" in euqation:
        operator = "**"
        n1,n2 = equation.split("**")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return
    if "+" in euqation:
        operator = "+"
        n1,n2 = equation.split("+")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return
    if "-" in equation:
        operator = "-"
        n1,n2 = equation.split("-")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return
    if "*" in equation:
        operator = "*"
        n1,n2 = equation.split("*")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return
    if "/" in equation:
        operator = "/"
        n1,n2 = equation.split("/")
        n1 = float(n1)
        n2 = float(n2)
        calculator(n1,n2,operator)
        return

