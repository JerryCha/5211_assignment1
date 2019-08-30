def plus(a,b):
    return [a[0] + b[0]]

def minus(a,b):
    return [a[0] - b[0]]

def divide(a,b):
    return [a[0] / b[0]]

def multiply(a,b):
    return [a[0] * b[0]]

def recursive_expr_eval(expr):
    assert len(expr) == 1 or len(expr) == 3
    #TODO write the rest of the program below
    '''
    if len(expr) == 1:
        return expr
    if len(expr[0]) == 3 and len(expr[2]) == 3:
        return expr[1](recursive_expr_eval(expr[0]), recursive_expr_eval(expr[2]))
    elif len(expr[0]) == 3 and len(expr[2]) == 1:
        return expr[1](recursive_expr_eval(expr[0]), expr[2])
    elif len(expr[0]) == 1 and len(expr[2]) == 3:
        return expr[1](recursive_expr_eval(expr[2]), expr[0])
    else:
        return expr[1](expr[0], expr[2])
    '''
    # expression length: 1, return itself
    if len(expr) == 1:
        return expr
    # From here, all evaluating operation is for the case where len(expr) == 3
    # Test the first expr, if it is an expression again, evaluate it.
    if len(expr[0]) == 3:
        operand1 = recursive_expr_eval(expr[0])
    # if not, it's an operand
    else:
        operand1 = expr[0]

    # The same process for the third expr.
    if len(expr[2]) == 3:
        operand2 = recursive_expr_eval(expr[2])
    else:
        operand2 = expr[2]
    
    # Do the computation.
    return expr[1](operand1, operand2)
    

expression1 = [[[12], divide, [3]], plus, [[6], minus, [1]]]
expression2 = [[[5], plus, [12]], multiply, [[3], plus, [0]]]
expressionplus = [expression1, plus, expression2]
expressionminus = [expression1, minus, expression2]
expressiondivide = [expression1, divide, expression2]
expressionmultiply = [expression1, multiply, expression2]

print(recursive_expr_eval(expression1))