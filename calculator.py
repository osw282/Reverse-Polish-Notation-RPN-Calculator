# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 11:27:04 2022

@author: Me
"""
def solve(exp, operators):
    temp = []
    
    for token in exp:
        if token.isdigit():
            temp.append(token)
        if token in operators and len(temp) < 2:
            raise ValueError("Invalid expression")
        elif token in operators and len(temp) > 1:
            val_2 = int(temp.pop())
            val_1 = int(temp.pop())
            if token == '+':
                temp.append(sum([val_1, val_2]))
            if token == '-':
                temp.append(val_1 - val_2)
            if token == '*':
                temp.append(val_1 * val_2)
            if token == '%':
                temp.append(val_1 % val_2)
            if token == '/':
                if val_2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                else:
                    temp.append(val_1 // val_2)
            
    return temp
    
def validate_input_type(exp, operators):
    for token in exp:
        if token.isdigit() or token in operators:
            continue
        else:
            raise TypeError("Only whole numbers and supported operations are allowed")

def validate_output(res):
    if len(res) > 1:
        raise ValueError("Invalid expression")
    else:
        res = res[0]
    if res < 0 or not str(res).isdigit():
        raise ValueError("Expression yeilds negative result")
    else:
        return res

if __name__ == "__main__":
    operators = {'+', '-', '*', '/', '%'} # Here specify the support opetators
    
    exp = input("Input an RPN expression: ") 
    exp = exp.split()

    validate_input_type(exp, operators)
    res = solve(exp, operators)
    
    print(f"Output: {validate_output(res)}")