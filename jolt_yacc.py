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
                 | print  
                 | function '''
    p[0] = p[1]



#brawta
def p_expression_plus(p):
    '''expression : expression PLUS term '''
    
    p[0] = p[1] + p[3]
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
#end of brawa

def p_statement_func(p):
    ''' function : FUNCTION IDENTIFIER OPENBRACE CLOSEBRACE
                 | FUNCTION IDENTIFIER OPENBRACE CLOSEBRACE'''

def p_expression_symbol(p):
    ''' expression : symbol'''
    p[0] = p[1]

def p_expr_symbols(p):
    ''' symbol : arithm_symbol 
               | compar_symbol'''
    
    p[0] = p[1]

def p_symbol_arithm(p):
    ''' arithm_symbol : PLUS
                      | MINUS
                      | DIVIDE
                      | TIMES '''
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
    '''expression : IDENTIFIER arithm_symbol term '''

    
    if p[2] == '+':
        p[0] = variables[p[1]] + p[3]
    elif p[2] == '-':
        p[0] = variables[p[1]] - p[3]
    elif p[2] == '/':
        p[0] = variables[p[1]] / p[3]
    else:
        p[0] = variables[p[1]] * p[3]



def p_expression_comparison(p):
    '''
    expression : factor compar_symbol factor '''
    
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
    else:
        p[0] = p[1] <= p[3]

def p_expression_comparison2(p):
    '''
    expression : IDENTIFIER compar_symbol IDENTIFIER
               | IDENTIFIER compar_symbol factor '''
    
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
        else:
            p[0] = variables[p[1]] <= variables[p[3]]
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
        else:
            p[0] = variables[p[1]] <= p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_term_times_div_factors(p):
    '''term : factor arithm_symbol factor '''
    
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

def p_factor_expr(p):
    'factor : OPENBRACE expression CLOSEBRACE' 
    p[0] = p[2]


def p_if_statement(p):
    '''
    if_statement : EF OPENBRACE expression CLOSEBRACE DEN statement
                 | EF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement
                 | EF OPENBRACE expression CLOSEBRACE DEN statement OREF OPENBRACE expression CLOSEBRACE DEN statement EFNOT statement

    '''
    if len(p) == 7:  # If there is no else clause
        if p[3]:
            p[0] = p[6]  # Execute the consequent statement
    elif len(p) == 9:  # If there is an else clause
        if p[3]:
            p[0] = p[6]  # Execute the consequent statement
        else:
           p[0] =  p[8]  # Execute the alternative statement
    else:
        if p[3]:
            p[0] = p[6]  # Execute the consequent statement
        elif p[9]:
            p[0] =  p[12]
        else:
            p[0]  = p[14]


def p_assign(p):
    '''
    assign : IDENTIFIER ASSIGNMENT NUMBA
            | IDENTIFIER ASSIGNMENT DECI
            | IDENTIFIER ASSIGNMENT WUD
            | IDENTIFIER ASSIGNMENT LETTA
            | IDENTIFIER ASSIGNMENT WHICHEVA
            | IDENTIFIER ASSIGNMENT expression
    '''
    # add the name of function,the identifier name and it's value to a tuple for further processing
    #p[0] = variables[p[1]] = p[3]
    variables[p[1]] = p[3]

# grammer for a show statement to show whatever is between the parenthesis
def p_print_show(p):
    '''
    print : SHOW OPENBRACE WUD CLOSEBRACE
          | SHOW OPENBRACE LETTA CLOSEBRACE
          | SHOW OPENBRACE IDENTIFIER CLOSEBRACE
    '''
    
    if p[3] in variables:
        p[0] = variables[p[3]]
    else:
        p[0] = p[3].strip('"')
 

def p_print_show2(p):
    '''
    print : SHOW OPENBRACE factor CLOSEBRACE
          
    '''   
    p[0] = p[3]

# def p_expression_logical(p):
#     '''
#     expression : expression AND expression
#                | expression OR expression
#                | expression NOT expression
#     '''

def p_error(p):
    print("Syntax Error: Input invalid")
    print(f"Syntax error at line {p.lineno}: {p.value}")



def parseifileinput(file):
    # Build the parser
    parser = yacc.yacc()

    print('_______________________________________________________________________________')
    while True:
        with open(file, 'r') as f:
            while True:
                for line in f.readlines():
                    print(line)
                    try:
                        s = line
                    except EOFError:
                        break
                    if not s: continue
                    result = parser.parse(s)
                    #print(result)
                    return result