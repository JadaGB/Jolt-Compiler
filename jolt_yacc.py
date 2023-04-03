# ------------------------------------------------------------
# Jolt Programming Language
# Jada Bailey & Garcian Mairs
# ------------------------------------------------------------
import os
import ply.yacc as yacc
from jolt_lex import * # Get the token map from the lexer. 
import sys
from pathlib import Path

import sys

# Dictionary to store variables and their values.
variables = {}
#List to store error and parse results messages
results = []

#set precedence for arithmetic operations
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

#Start of Grammar
def p_program(p):
    'program : statement'
    p[0] = p[1]
    print('program_statement',p[1])

#Grammar Rules & Possible Derivations
def p_statement(p):
    '''statement : expression
                 | if_statement
                 | loop
                 | assign
                 | print
                 | COMMENT '''
    p[0] = p[1]
    print('statement')

def p_stmt2(p):
    '''statement : statement COMMA statement '''
    a = []
    if p[1] != None:
        a.append(p[1])
    a.append(p[3])
    p[0] = a

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
    print('arithmetic_statement',p[2],p[1],p[3])

def p_expression_symbol(p):
    ''' expression : symbol'''
    p[0] = p[1]
    print('expression-symbol',p[1])

def p_expression_stmt_types(p):
    ''' expression : compar_stmt
                   | arith_stmt'''
    p[0] = p[1]
    print('expression-statement',p[1])

def p_expr_symbols(p):
    ''' symbol : arithm_symbol 
               | compar_symbol'''
    
    p[0] = p[1]
    print('symbol',p[1])

def p_symbol_arithm(p):
    ''' arithm_symbol : PLUS
                      | MINUS
                      | DIVIDE
                      | TIMES
                      | MODULUS '''
    p[0] = p[1]
    print('arithmetic_symbol',p[1])

def p_symbol_comparison(p):
    ''' compar_symbol : GREATER_THAN
                      | LESS_THAN
                      | EQUAL
                      | NOT_EQUAL
                      | GREATER_EQUAL
                      | LESS_EQUAL '''
    p[0] = p[1]
    print('comparative_symbol',p[1])

def p_expression_withidentifier(p):
    '''arith_stmt : IDENTIFIER arithm_symbol term
                  | IDENTIFIER error term'''
    try:
        if p[2] == '+':
            if type(p[1]) == str and type(p[3]) == str:
                p[0] = variables[p[1]].strip('"') + p[3].strip('"')
            else:
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
    except TypeError:
        results.append("Type Error: Invalid pair of data types for operation")
    except AttributeError:
        results.append("Attribute Error: Invalid data types for operation")
    except KeyError:
        results.append("Key Error: Error accessing identifier!")
    print('arithm-stmt',p[1],p[3])

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
    print('compar-stmt',p[2],p[1],p[3])

def p_expression_comparison2(p):
    '''
    compar_stmt : IDENTIFIER compar_symbol IDENTIFIER
                | IDENTIFIER compar_symbol factor
                | IDENTIFIER error factor
                | IDENTIFIER error IDENTIFIER'''
    try:
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
    except KeyError:
        results.append("Key Error: Error Accessing Identifier!")
    except TypeError:
        results.append("Type Error: Invalid pair of data types for operation")
    print('compar_stmt',p[2],p[1],p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    print('expression-term',p[1])

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    print('term-factor',p[1])

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
    print('arith_symbol',p[2],p[1],p[3])

def p_factor_digit(p):
    '''
    factor : NUMBA
            | DECI
    '''
    p[0] = p[1]
    print("factor",p[1])

def p_term_factor_iden(p):
    'term : IDENTIFIER'
    try:
        p[0] = variables[p[1]]
    except KeyError:
        results.append("Key Error: Error accessing identifier!")
    print('term-identifier',p[1])

def p_factor_expr(p):
    'factor : OPENBRACE expression CLOSEBRACE' 
    p[0] = p[2]
    print('factor',p[1],p[2],p[3])

def p_if_statement(p):
    '''
    if_statement : DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE compar_stmt CLOSEBRACE DEN statement OREF OPENBRACE compar_stmt CLOSEBRACE DEN statement EFNOT statement DOUBLE_GREATER
                 | DOUBLE_LESS EF OPENBRACE error CLOSEBRACE DEN statement DOUBLE_GREATER
    '''
    #Executes if the EF statement has an EFNOT or OREF portion
    if len(p) == 9:  
        #if the condition is true
        if p[4]: 
            #Execute the consequent statement
            p[0] = p[7]  
            print('if_statement',p[2],p[4],p[7])
    #Executes if the EF statement has an EFNOT portion
    elif len(p) == 11:  
        #if the first condition is true
        if p[4]: 
            #Execute the consequent statement
            p[0] = p[7]  
            print('if_statement',p[2],p[4],p[7])
        #if the condition is false
        else: 
           #Execute the alternative statement
           p[0] =  p[9] 
           print('if_statement',p[2],p[4],p[7],p[8],p[9])
    #Executes if the EF statement has an OREF portion
    elif len(p) == 17: 
        #if the first condition is true
        if p[4]: 
            #Execute the consequent statement
            p[0] = p[7] 
            print('if_statement',p[2],p[4],p[7])
        #if the second condition is true
        elif p[10]: 
            p[0] =  p[13]
            print('if_statement',p[2],p[4],p[7],p[8],p[10],p[13],p[14],p[15])
        #if none of the conditions are true
        else: 
            p[0] = p[15]
            print('if_statement',p[2],p[4],p[7],p[8],p[10],p[13],p[14],p[15])
    else:
        results.append("Error: Invalid IF Statement.") 
    

def p_statement_forloop(p):
    '''loop : DOUBLE_LESS WEN IDENTIFIER IN expression COLON statement DOUBLE_GREATER
            | DOUBLE_LESS WEN IDENTIFIER IN expression COMMA expression COLON statement DOUBLE_GREATER'''
    try:
        if len(p) == 9:
            for p[3] in range(p[5]):
                # results.append("loop")
                results.append(p[7])
            print('loop',p[2],p[3],p[5],p[7])
        elif len(p) == 11:
            for p[3] in range(p[5],p[7]):
                # results.append("loop")
                results.append(p[9])
            print('loop',p[2],p[3],p[5],p[7],p[9])
        else:
            results.append("Error: Invalid Wen Loop.")
    except TypeError:
        results.append("Type Error: Invalid Wen Loop.")
    except IndexError:
        results.append(" Index Error: Wen Loop Out of Bounds.")
    
      
def p_assign(p):
    '''
    assign : IDENTIFIER ASSIGNMENT expression
           | IDENTIFIER ASSIGNMENT WUD
           | IDENTIFIER ASSIGNMENT LETTA
    '''
    variables[p[1]] = p[3]
    print('assign',p[1],p[3])

def p_print_show(p):
    '''
    print : SHOW OPENBRACE IDENTIFIER CLOSEBRACE
    '''
    if p[3] in variables:
        p[0] = variables[p[3]]
    else:
        results.append("Null Value Error: Identifier Needs Initiaization.")
    print('print',p[1],p[3])
        
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
    print('print',p[1],p[3])

def p_error(p):
    results.append("Syntax Error: Input invalid")
    if p is None:
        results.append("Error: Missing Token From Syntax")
    else:
        results.append(f"Syntax Error at : {p.value}")

def parseInput(content):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Build the parser
    parser = yacc.yacc()
    variables.clear()
    results.clear()
    lineNum = 0

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
                            results.append("Index out of bound when reading program")
                            break
            if "~" in s: #ignores comments and does not parse them
                continue
            # if "loop" in s: #does not append loop results in this function
            #     parser.parse(s)
            # else:
            result = parser.parse(s)
            if result != "" and result != None: #does not append null results
                results.append(result)
            lineNum = lineNum + 1
            # print(variables)
        return results