# ------------------------------------------------------------
# Jolt Programming Language
#Jada Bailey & Garcian Mairs
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required

reserved = {
   'ef' : 'EF',
   'den' : 'DEN',
   'efnot' : 'EFNOT',
   'oref' : 'OREF',
   'numba':'numba',
   'deci':'deci',
   'wud':'wud',
   'letta':'letta',
   'show' : 'SHOW',
}

digits=[
     'NUMBA',
     'DECI',
]

arithmetic_op =[
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'MODULUS'
]

conditional_op = [
    #Comparative/Conditional Operators
   'EQUAL',
   'NOT_EQUAL',
   'GREATER_THAN',
   'LESS_THAN',
   'GREATER_EQUAL',
   'LESS_EQUAL',
]

tokens = [

    'IDENTIFIER',
    #Literals
#    'NUMBA',
#    'DECI',
   'WUD',
   'LETTA',
   'WHICHEVA',

    #Logical Operators
   'AND',
   'OR',
   'NOT',

   #Symbols
   'ASSIGNMENT',
   'END_LINE',
   'COMMENT',
   'COLON',
   'OPENBRACE',
   'CLOSEBRACE',
   'DOUBLE_LESS',
   'DOUBLE_GREATER',
] + list(reserved.values()) + arithmetic_op + conditional_op + digits

#Regular Expressions for Tokens - Simple
# t_INCREMENT  = r'\+\+'
# t_DECREMENT  = r'\-\-'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MODULUS = r'%'

t_AND  = r'\@'
t_OR  = r'\|'
t_NOT  = r'\?'

t_EQUAL    = r'\=\='
t_NOT_EQUAL   = r'\?\='
t_GREATER_THAN  = r'\>'
t_LESS_THAN  = r'<'
t_GREATER_EQUAL  = r'\>='
t_LESS_EQUAL  = r'\<='

t_COLON   = r'\:'
t_ASSIGNMENT    = r'\='
t_END_LINE   = r'\.'
t_OPENBRACE  = r'\('
t_CLOSEBRACE  = r'\)'
t_DOUBLE_LESS = r'\<\<'
t_DOUBLE_GREATER = r'\>\>'


#Regular Expressions for Tokens - Functions
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_DECI(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBA(t):
    r'([0-9]+)' 
    t.value = int(t.value)  
    return t

def t_LETTA(t):
    r'"([a-zA-Z]?)"'
    t.value = t.value
    return t

def t_WUD(t):
    #Starts & ends with a double quote
    # [^"\\] matches any character that is not a double quote or a backslash.
    # | is the alternation operator, which means "or".
    # \\. matches an escaped character (e.g., \" or \\).
    r'"([^"\\]|\\.)*"'
    t.value = t.value
    return t

def t_WHICHEVA(t):
    r'False' #Need to fix
    t.value = bool(t.value)
    return t

def t_COMMENT(t):
    r'~.*~'
    t.value = t.value
    pass

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# precedence = (
#     ('left', 'PLUS', 'MINUS'),
#     ('left', 'TIMES', 'DIVIDE'),
# )
# Error handling rule
def t_error(t):
    print("\033[1;31mIllegal character: '%s' \033[0m" % t.value[0] )
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

data = ''' '''

#'''3.1'''
#check for 3 + 4 * 10 + - 20
#epr + term
#term + term
#factor + term
#factor + term
#factor + term * factor
#factor + factor * factor
#num + num+ num = syntax correct

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok) #-prints token type, value, position
    print(tok.type,':', tok.value)