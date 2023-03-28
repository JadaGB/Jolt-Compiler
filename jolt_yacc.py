import os
import ply.yacc as yacc
from jolt_lex import * # Get the token map from the lexer. 
import sys
from pathlib import Path

filepath = Path(__file__).parent / "sample.jolt"
# sys.path.append(r'C:\Users\river\Downloads\APL\APL\Jolt-Compiler')

import sys

# Dictionary to store variables and their values.
variables = {}
#List to store error messages
results = []

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

def p_program(p):
    'program : statement'
    p[0] = p[1]

# Define the rule for a statement, which can be a simple expression or a control structure
def p_statement(p):
    '''statement : expression
                 | if_statement
                 | assign
                 | print '''
    p[0] = p[1]

#brawta
def p_expression_plus(p):
    '''arith_stmt : expression arithm_symbol expression
                   | expression error term'''
    try:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            if p[3] == 0:
                raise ZeroDivisionError()
            else:
                p[0] = p[1] / p[3]
        elif p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
        elif p[2] == '%':
            p[0] = p[1] % p[3]
        elif p[2] in conditional_op: 
            results.append("Error: Unexpected Comparative Symbol!")
        else:
            results.append("Error: Invalid Arithmetic Symbol!")
    except ZeroDivisionError:
        results.append("Zero Division Error: Cannot divide by zero.")
    except TypeError:
       results.append("Type Error: Expected Numba or Deci.")

def p_expression_symbol(p):
    ''' expression : symbol'''
    p[0] = p[1]

def p_expression_stmt_types(p):
    ''' expression : compar_stmt
                   | arith_stmt'''
    p[0] = p[1]

def p_expr_symbols(p):
    ''' symbol : arithm_symbol 
               | compar_symbol'''
    
    p[0] = p[1]

def p_symbol_arithm(p):
    ''' arithm_symbol : PLUS
                      | MINUS
                      | DIVIDE
                      | TIMES
                      | MODULUS '''
    p[0] = p[1]

def p_symbol_comparison(p):
    ''' compar_symbol : GREATER_THAN
                      | LESS_THAN
                      | EQUAL
                      | NOT_EQUAL
                      | GREATER_EQUAL
                      | LESS_EQUAL '''
    p[0] = p[1]

def p_expression_withidentifier(p):
    '''arith_stmt : IDENTIFIER arithm_symbol term
                  | IDENTIFIER error term'''
    try:
        if p[2] == '+':
            p[0] = variables[p[1]] + p[3]
        elif p[2] == '-':
            p[0] = variables[p[1]] - p[3]
        elif p[2] == '*':
            p[0] = variables[p[1]] * p[3]
        elif p[2] == '/':
            if p[3] == 0:
                raise ZeroDivisionError()
            else:
                p[0] = variables[p[1]] / p[3]
        elif p[2] in conditional_op: 
            results.append("Error: Unexpected Comparative Symbol!")
        else:
            results.append("Error: Invalid Arithmetic Symbol!")
    except ZeroDivisionError:
        results.append("Zero Division Error: Cannot divide by zero.")

def p_expression_comparison(p):
    '''
    compar_stmt : factor compar_symbol factor
                | factor error factor'''
    if p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '?=':
        p[0] = p[1] != p[3] 
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    else:
        results.append("Error: Invalid Comparison Symbol!")

def p_expression_comparison2(p):
    '''
    compar_stmt : IDENTIFIER compar_symbol IDENTIFIER
                | IDENTIFIER compar_symbol factor
                | IDENTIFIER error factor
                | IDENTIFIER error IDENTIFIER'''
    
    if p[3] in variables:
        if p[2] == '>':
            p[0] = variables[p[1]] > variables[p[3]]
        elif p[2] == '<':
            p[0] = variables[p[1]] < variables[p[3]]
        elif p[2] == '==':
            p[0] = variables[p[1]] == variables[p[3]]
        elif p[2] == '?=':
            p[0] = variables[p[1]] != variables[p[3]]
        elif p[2] == '>=':
            p[0] = variables[p[1]] >= variables[p[3]]
        elif p[2] == '<=':
            p[0] = variables[p[1]] <= variables[p[3]]
        else:
            results.append("Error: Invalid Comparison Statement.")
    else:
        if p[2] == '>':
            p[0] = variables[p[1]] > p[3]
        elif p[2] == '<':
            p[0] = variables[p[1]] < p[3]
        elif p[2] == '==':
            p[0] = variables[p[1]] == p[3]
        elif p[2] == '?=':
            p[0] = variables[p[1]] != p[3] 
        elif p[2] == '>=':
            p[0] = variables[p[1]] >= p[3]
        elif p[2] == '<=':
            p[0] = variables[p[1]] <= p[3]
        elif p[2] in conditional_op: 
            results.append("Error: Invalid Comparative Statement!")
        else:
            results.append("Error: Unexpected Arithmetic Symbol!")

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_term_times_div_factors(p):
    '''arith_symbol : factor arithm_symbol factor '''
    
    if p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    else:
        p[0] = p[1] - p[3]

def p_factor_digit(p):
    '''
    factor : NUMBA
            | DECI
    '''
    p[0] = p[1]

def p_term_factor_iden(p):
    'term : IDENTIFIER'
    p[0] = variables[p[1]]

def p_factor_expr(p):
    'factor : OPENBRACE expression CLOSEBRACE' 
    p[0] = p[2]


def p_if_statement(p):
    '''
    if_statement : DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement OREF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE error CLOSEBRACE DEN statement DOUBLE_GREATER
    '''
    # print("\033[1;31mInvalid IF Statement.\033[0m") 

    if len(p) == 9:  # If there is no else clause
        if p[4]:
            p[0] = p[7]  # Execute the consequent statement
    elif len(p) == 11:  # If there is an else clause
        if p[4]:
            p[0] = p[7]  # Execute the consequent statement
        else:
           p[0] =  p[9]  # Execute the alternative statement
    elif len(p) == 17:
        if p[4]:
            p[0] = p[7]  # Execute the consequent statement
        elif p[10]:
            p[0] =  p[13]
        else:
            p[0]  = p[15]
    else:
        results.append("Error: Invalid IF Statement.") 
    # else:
    #     raise SyntaxError(error_messages['syntax_error'].format(tokens.lineno, tokens.value))
            
def p_assign(p):
    '''
    assign : IDENTIFIER ASSIGNMENT expression
            | IDENTIFIER ASSIGNMENT WUD
            | IDENTIFIER ASSIGNMENT LETTA
            | IDENTIFIER ASSIGNMENT WHICHEVA
    '''
    # add the name of function,the identifier name and it's value to a tuple for further processing
    #p[0] = variables[p[1]] = p[3]
    p[0] = ""
    variables[p[1]] = p[3]

# grammer for a show statement to show whatever is between the parenthesis
def p_print_show(p):
    '''
    print : SHOW OPENBRACE IDENTIFIER CLOSEBRACE
    '''
    if p[3] in variables:
        p[0] = variables[p[3]]
    else:
        results.append("Null Value Error: Identifier Needs Initiaization.")
        
def p_print_show2(p):
    '''
    print : SHOW OPENBRACE factor CLOSEBRACE
          | SHOW OPENBRACE WUD CLOSEBRACE
          | SHOW OPENBRACE LETTA CLOSEBRACE
          | SHOW OPENBRACE error CLOSEBRACE
    '''   
    if len(p) == 5:
        if type(p[3]) == int or type(p[3]) == float:
            p[0] = p[3]
        if type(p[3]) == str:
            p[0] = p[3].strip('"')
    else:
       results.append("Error: Invalid Show Statement.")

# def p_accept_input_statement(p):
#     '''
#     accept_input : IDENTIFIER ASSIGNMENT SHOW OPENBRACE WUD CLOSEBRACE COLON
#     '''
#     p[0] = ""
#     variables[p[1]] = int(input(p[5]))

    # if p[8] == "numba":
    #     variables[p[1]] = int(input(p[5]))
    # elif p[8] == "deci":
    #     variables[p[1]] = float(input(p[5]))
    # elif p[8] == "wud":
    #     variables[p[1]] = str(input(p[5]))
    # elif p[8] == "letta":
    #     variables[p[1]] = input(p[5])
    # else:
    #     results.append("Identifier Error: Reserved Word Cannot Be An Identifier")
# def p_expression_logical(p):
#     '''
#     expression : expression AND expression
#                | expression OR expression
#                | expression NOT expression
#     '''

def p_error(p):
    results.append("Syntax Error: Input invalid")
    if p is None:
        results.append("Error: Missing Token From Syntax")
    else:
        results.append(f"Syntax Error at line {p.lineno}: {p.value}")

os.system('cls' if os.name == 'nt' else 'clear')

def parseInput(content):
    # Build the parser
    parser = yacc.yacc()
    results.clear()
    # results = []
    lineNum = 0

    print('_______________________________________________________________________________')
    while True:
        for lines in content:
            s = lines
            
            if "<<" in s:
                if len(content) > 1:
                    while True:
                        try:
                            if ">>" in s:
                                break
                            else:
                                nextline =  content[lineNum+1]
                                s = s + nextline
                                del content[lineNum+1]

                                if ">>" in s:
                                    break
                        except IndexError:
                            print("Index out of bound when reading program")

            print(s)
            # if ":" in s:
            #     parser.ply.yield_()
            result = parser.parse(s)
            if result != "" and result != None:
                results.append(result)
            lineNum = lineNum + 1
        return results