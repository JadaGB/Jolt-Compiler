import os
import ply.yacc as yacc

# Get the token map from the lexer. 
from jolt_lex import tokens

def p_literal(p):
    '''
    literal : NUMBA
              | DECI
              | LETTA
              | WUD
    '''
    p[0] = ('literal', p[1])

def p_symbol(p):
    '''
    symbol :  ASSIGNMENT
              | END_LINE
              | COMMENT
              | COLON
              | OPENBRACE
              | CLOSEBRACE
              | DOUBLE_LESS
              | DOUBLE_GREATER
    '''
    p[0] = ('symbol', p[1])

# def p_expression_plus(p):
#     'expression : expression PLUS factor'
#     p[0] = p[1] + p[3]

# def p_expression_factor(p):
#     'expression : factor'
#     p[0] = p[1]

# def p_factor_num(p):
#     'factor : NUMBA'
#     p[0] = p[1]

def p_error(p):
    print("Syntax Error: Input invalid")

# Build the parser
parser = yacc.yacc()

print('...............................Welcome to Jolt Terminal................................')
while True:
   try:
       s = input('Jolt >> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)