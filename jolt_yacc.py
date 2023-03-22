import ply.yacc as yacc
from jolt_lex import tokens # Get the token map from the lexer. 

import sys

# Dictionary to store variables and their values.
variables = {}

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

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_comparison(p):
    '''
    expression : NUMBA GREATER_THAN NUMBA
    '''
    p[0] = p[1] > p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_digit(p):
    '''
    factor : NUMBA
            | DECI
    '''
    p[0] = p[1]

def p_factor_expr(p):
    'factor : OPENBRACE expression CLOSEBRACE'
    p[0] = p[2]

# grammer for setting defining a variable and set it's value
def p_assign(p):
    '''
    assign : LET IDENTIFIER ASSIGNMENT NUMBA
            | LET IDENTIFIER ASSIGNMENT DECI
            | LET IDENTIFIER ASSIGNMENT WUD
            | LET IDENTIFIER ASSIGNMENT LETTA
            | LET IDENTIFIER ASSIGNMENT WHICHEVA
    '''
    # add the name of function,the identifier name and it's value to a tuple for further processing
    p[0] = ('LET', p[2], p[4])
    variables[p[2]] = p[4]
    # variables[p[1]] = p[3]
    

def p_if_statement(p):
    '''
    if_statement : IF OPENBRACE expression CLOSEBRACE COLON statement
                 | IF OPENBRACE expression CLOSEBRACE COLON statement ELSE COLON statement
    '''
    if len(p) == 7:  # If there is no else clause
        if p[3]:
            p[6]()  # Execute the consequent statement
    else:  # If there is an else clause
        if p[3]:
            p[6]()  # Execute the consequent statement
        else:
            p[8]()  # Execute the alternative statement
    # if (len(p) == 7):
    #     p[0] = (p[3])
    #     if(p[0]==True):
    #         p[6]
    #     else:
    #         p[9]
    # else:
    #     p[0] = (p[3])
    #     if(p[0]==False):
    #         p[9]
    # return [0]
    # if p[3]:
    #     print("The condition in the if statement is true")
    #     p[6]
    # else:
    #     print("The condition in the if statement is false")
    #     p[9]
# Define the rule for an if statement, which consists of a condition and one or more statements
# def p_if_statement(p):
#     'if_statement : IF OPENBRACE expression CLOSEBRACE DOUBLELESS program DOUBLEGREATER'
#     p[0] = ('if', p[3], p[6])

# grammer for a print statement to print whatever is between the parenthesis
def p_print(p):
    '''
    print : PRINT OPENBRACE expression CLOSEBRACE
          | PRINT OPENBRACE IDENTIFIER CLOSEBRACE
    '''
    print(variables[p[3]])
    return ""
    # print(p[3])
    

# Define the parsing rules
# def p_statement_if(p):
#     'statement : IF OPENBRACE expression CLOSEBRACE DUH DOUBLESS expression DOUBLEGREATER'

# Error rule for syntax errors
def p_error(p):
    print("Syntax Error: Input invalid")
    print(f"Syntax error at line {p.lineno}: {p.value}")

# Build the parser
parser = yacc.yacc()

print('_______________________________________________________________________________')
while True:
   try:
       s = input('Jolt >> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)